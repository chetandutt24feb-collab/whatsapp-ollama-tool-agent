import datetime
import json
from flask import Flask
import ollama
from images_send import get_next_two_images,get_budget
import requests



# Hamari bina change ki hui calendar file se functions ko import karein
from consultation import create_event



app = Flask(__name__)
a=0
# Ollama Client setup
client = ollama.Client(host="http://localhost:11434")

def ollama_calling(message,from_number,message_history,available_tools1,VERIFY_TOKEN,ACCESS_TOKEN,PHONE_NUMBER_ID):
    available_tools=available_tools1
    message_history=message_history
    a=0
 # AI ko batane ke liye ki hamare paas ye dono tools maujood hain
 #available_tools = available_tools

    # User ka message history me jodein
    #messages_history[from_number].append({"role": "user", "content": user_input})

    try:
        # LLM se response maangein tools ke sath
        response = client.chat(
            model="gemma4:31b-cloud",
            messages= message_history[from_number],
            tools=available_tools,
        )

        # Check karein ki kya AI koi function run karna chahta hai
        if response.get("message", {}).get("tool_calls"):
            for tool in response["message"]["tool_calls"]:
                tool_name = tool["function"]["name"]
                args = tool["function"]["arguments"]

                message_history[from_number].append(response["message"]) 
                a=a+1
                print(f"\n⚙️ [AI Triggered Tool]: {tool_name}")
                #messages_history[from_number].append({"role": "system", "content": tool_name})

                # 1. Free slots nikalne ka tool logic
             
                # . Event book karne ka tool logic
                if tool_name == "book_project_appointment":
                    # Arguments ko sahi dict format me pack karna jaisa create_event ko chahiye
                    meeting_date = {
                        'year': int(args.get("year")),
                        'month': int(args.get("month")),
                        'day': int(args.get("day")),
                    }
                    meeting_time = {
                        'hours': int(args.get("hours")),
                        'minutes': int(args.get("minutes")),
                        'seconds': 0,
                    }
                    meeting_type= args.get("type") or args.get("meeting_type") or args.get("mode") or "Online"

                    # Direct calender_logic ka function call
                    event_result = create_event(
                        meeting_date,meeting_time,from_number,meeting_type
                    )
                    
                    tool_output = f"{event_result}!"
                    message_history[from_number].append({"role": "tool","content": tool_output,
                        "name": tool_name,})
                    a=a+1
               
                elif tool_name == "get_budget":
                    try:
                        # LLM se extract kiya hua bhk_type parameter uthana (jaise "1", "2", "3", "4")
                        bhk = args.get("bhk_type")
                        print(f"💰 [AI Triggered Budget] Fetching details for: {bhk} BHK")
                        
                        # Aapka budget calculation method call
                        budget_result = get_budget(bhk)
                        
                        tool_output = f"Estimated budget and cost details for a {bhk} BHK project are as follows: {budget_result}"
                    except Exception as e:
                        print(f"Error in get_budget tool: {e}")
                        tool_output = "An internal server error occurred while retrieving the budget calculation data."
                        
                    # Tool ka response message history me jodna
                    message_history[from_number].append({
                        "role": "tool",
                        "content": tool_output,
                        "name": tool_name
                    })
                    a = a + 1
                elif tool_name=="get_project_images":
                 try:
                  
                  res = requests.post(
                     f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                     headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                     json={
                          "messaging_product": "whatsapp",
                          "to": from_number,
                          "type": "text",
                          "text": {
                            "body": "Here are some of our premium designs curated exclusively for you: ✨"
                            }
                        }
        )        
                  print("inside get project images")
                  images=get_next_two_images(from_number)
                  print(f"{images}")
                
                  for img in images:
                     print(f"{img}")
                     image_payload = {
                            "messaging_product": "whatsapp",
                            "to": from_number,
                            "type": "image",
                            "image": {
                                "link": img,  
                            }
                        } 
                     img_res = requests.post(
                                  f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                                  headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                                  json=image_payload
                                 ) 
                     print(f"Image Send Status: Response: ")
                   
                  tool_output = "Images have been shared successfully. Please proceed with the conversation."
                 except Exception as e:
                   tool_output = "An internal server error occurred while attempting to share the images."
                   
                 
                 

                 
                 message_history[from_number].append({"role": "tool","content": tool_output,
                        "name": tool_name,})
                 a=a+1
                elif tool_name=="get_project_videos":
                 try:
                  res = requests.post(
                     f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                     headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                     json={
                          "messaging_product": "whatsapp",
                          "to": from_number,
                          "type": "video",
                          "video": {
                            "link":"VIDEO_LINK",
                            "caption": "Here are some of our exclusive designs for you: ✨"
                            }
                        }
        )
                  tool_output="The video has been successfully sent to the user!" 
                 except Exception as e:
                    tool_output="An internal server error occurred while trying to load the video!"
                
                 message_history[from_number].append({"role": "tool","content": tool_output,
                        "name": tool_name,})
                 a=a+1
                else:
                    tool_output = "Tool nahi mila."
                    message_history[from_number].append({"role": "tool","content": tool_output,
                        "name": tool_name,})
                    a=a+1
                # Tool ka output wapas AI ko dein taaki wo badhiya Hinglish me answer de sake
                

                # AI ko final response banane ke liye dubara call karein
                final_response = client.chat(
                    model="gemma4:31b-cloud", messages=message_history[from_number]
                )
                reply_message = final_response["message"]["content"]
                message_history[from_number].append(
                    {"role": "assistant", "content": reply_message}
                )
                a=a+1
                j=1
                while j<=a and len(message_history[from_number])>=15 :
                   message_history[from_number].pop(1)
                   j=j+1
                
                return { "messaging_product": "whatsapp",
                         "to": from_number,
                         "type": "text",
                         "text": {"body": reply_message}
                }
               

        else:
            # Agar koi tool call nahi hua, toh normal chit-chat karein
            reply_message = response["message"]["content"]
            a=a+1 
            j=1
            message_history[from_number].append(
                {"role": "assistant", "content": reply_message}
            )
           # while j<=a and len(message_history[from_number])>=15 :
            #       message_history[from_number].pop(1)

            return { "messaging_product": "whatsapp",
                         "to": from_number,
                         "type": "text",
                         "text": {"body": reply_message}
                }
            

    except Exception as e:
       print(f"error is{e}")
                