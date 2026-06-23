from flask import Flask, request, jsonify
import requests
import sys
import json
import time
import my_ollama 
from datetime import datetime
from pymongo import MongoClient
import yt_dlp
import threading

app = Flask(__name__)

with open("D:/python/WHATSAPP BOT USING META API/config.json",encoding="utf-8") as f:
   variable=json.load(f)


VERIFY_TOKEN=variable["VERIFY_TOKEN"]
ACCESS_TOKEN=variable["ACCESS_TOKEN"]
PHONE_NUMBER_ID=variable["PHONE_NUMBER_ID"]
MONGO_URI=variable["MONGO_URI"]
OUR_PHONE=variable["OUR_PHONE"]

message_history={}
message_history1={}



client = MongoClient(MONGO_URI)

retry_count=0
def connectingToMongo(retry_count):
 if retry_count<=3:
  db = client["chat_history"]
  chats_collection = db["ollama"]
  chats_collection2=db["chats"]
  try:
    client.admin.command('ping')
    print("MongoDB se successfully connect ho gaye hain!")
    query={"file_name":"system_instruction.txt"}
    result = chats_collection.find_one(query)
    prompt=result["file_data"]
 #print("result fetched for system instruction")

    query={"file_name":"available_tools.json"}
    result = chats_collection.find_one(query)
    available_tools = result["file_data"]
    return {"available_tools":available_tools,"chats_collect2":chats_collection2,"prompt":prompt}
  except Exception as e:
   
   print(f"error {e}")
   time.sleep(1)
   a=connectingToMongo(retry_count+1)
   return a
 else:
   
   return None

output=connectingToMongo(retry_count)

if output is not None:
 available_tools=output["available_tools"]
 chats_collection2=output["chats_collect2"]
 prompt=output["prompt"]

else:
  print("abhi server issue hai")
  sys.exit()


 
@app.route('/webhook', methods=['POST'])
def webhook():
 data = request.get_json()
 try:
        if "messages" not in data["entry"][0]["changes"][0]["value"]:
            return "OK", 200  # Agar sirf deliver/read status hai toh skip
 except Exception:
        return "OK", 200
 def knownNumber(data):
    try:
        
        if 'messages' in data['entry'][0]['changes'][0]['value']:
            message=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            from_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
            #print(from_number)
            
            if from_number in OUR_PHONE :
               #print("number found")
             
               query = message

               with yt_dlp.YoutubeDL({"extract_flat": True,"quiet": True}) as ydl:
                result = ydl.extract_info(
                f"ytsearch3:{query}",
                   download=False
                     )

               if result and "entries" in result:
                  print(f"--- Top 3 Results for '{query}' ---\n")
                  len=1
                  url=""
                  for i, video in enumerate(result["entries"], start=1):
                       #print(f"{i}. {video.get('title')}")
                       url= f"{url} {video.get('title')} "+ f"https://www.youtube.com/watch?v={video.get('id')}\n" 
                       len=len+1
                  res=requests.post(
                        f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                        headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                        json={ "messaging_product": "whatsapp",
                         "to": from_number,
                         "type": "text",
                         "text": {"body":  f"{url} \n"}
                         }
                        ) 
               return
             
             
               
                
             

            if from_number not in message_history:
             message_history[from_number]=[{'role':'system','content':prompt  }]
             query={"user_id":from_number}
             result = chats_collection2.find(query).sort("timestamp", -1).limit(12)
             for doc in result:
               message_history[from_number].insert(1,{'role':doc.get('role'),'content':doc.get('file_data')})
            #message_history1[from_number]=[{'role':'system','content':prompt}]
            #message_history[from_number].append({'role':'user','content':message})
            data_to_insert = {
            "user_id": from_number,
            "role":"user",
            "file_data": message, # Saara text yahan save hoga
            "description": "user chats",
            "timestamp": datetime.now()
     }
            #print(message_history)
            def updatetodb():
             result = chats_collection2.insert_one(data_to_insert)
            threading.Thread(target=updatetodb).start()
            
            current_time_str = datetime.now().strftime("%d-%m-%Y %H:%M")
            formatted_input = f"{message} (Message Sent Time: {current_time_str})"
            message_history[from_number].append({'role': 'user', 'content': formatted_input})
            #print(message_history)

            
            json2=my_ollama.ollama_calling(message,from_number,message_history,available_tools,VERIFY_TOKEN,ACCESS_TOKEN,PHONE_NUMBER_ID)
            data_to_insert = {
            "user_id": from_number,
            "role":"system",
            "file_data": json2["text"]["body"], # Saara text yahan save hoga
            "description": "user chats",
            "timestamp": datetime.now()
     }
            result = chats_collection2.insert_one(data_to_insert)
            res=requests.post(
                f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                json=json2
            )
            #print(f"Status: {res.status_code}")
            #print(f"Meta Response: {res.json()}")
    except Exception as e:
        data_to_insert = {
            "user_id": from_number,
            "role":"system",
            "file_data": f"{e}", # Saara text yahan save hoga
            "description": "user chats",
            "timestamp": datetime.now()
    }
        #result = chats_collection2.insert_one(data_to_insert)
        return requests.post(
                f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
                headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
                json={ "messaging_product": "whatsapp",
                         "to": from_number,
                         "type": "text",
                         "text": {"body": "Sorry I Cannot Answer Your Query Write Now!! "}
                }
               )
                
 threading.Thread(target=knownNumber,args=(data,)).start()

 return "OK", 200

if __name__ == '__main__':
    app.run(port=5000,threaded=True)