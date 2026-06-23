from typing import Any, Dict, List

# Aapki saari Cloudinary images ki main list

def get_next_two_images(phone_number):
      CLOUDINARY_IMAGES: List[str] = [
      "IMAGES_URL"]

# Har user ka track rakhne ke liye global dict pointer (Key: phone_number, Value: current_index)
      print("url shared of cloudinary to my_ollama file")
      return CLOUDINARY_IMAGES

def get_budget(size):
 try:
      size=int(size)      
      if size==1:
            return """ ✨ *Your Interior Design Estimate Summary* ✨\nWe've prepared 3 lifestyle options for your home:\n*ESSENTIAL - ₹4.5 Lakh*\n Ideal for rental properties\n* Kitchen: ₹1.5 Lakh\n* Wardrobe: ₹74,539\n
* Other interiors: ₹2.2 Lakh\n_*Specs*: Aquashield, Solid finishes and Tyrox hardware_\n*COMFORT [Popular] - ₹6.6 Lakh*
\n> Perfect for first-time homeowners
\n* Kitchen: ₹.2 Lakh
\n* Wardrobe: ₹,519
\n* Other interiors: ₹.5 Lakh
\n_*Specs*: Hydroguard+, Hi Gloss Finishes and Tyrox hardware_

\n*LUXURY - ₹.5 Lakh*
\n> Best of design and style
\n* Kitchen: .5 Lakh
\n* Wardrobe: ₹.1 Lakh
\n* Other interiors: ₹.8 Lakh
\n_*Specs*: BWP ply with Glass/Acrylic/Lacquard finishes and Hettich/Hafele hardware_

\n*Common Kitchen Details*:
\n* Shape: L-shaped
\n* Size: 9ft 3inch x 1ft 1inch

\nNote: This is an approximate estimate based on your selections and may change depending on your space dimensions, design choices, customizations, or additional work requested."""              
      if size==2:
            return """✨ *Your Interior Design Estimate Summary* ✨\n
\nWe've prepared 3 lifestyle options for your home:

\n*ESSENTIAL - ₹.2 Lakh*
\n> Ideal for rental properties
\n* Kitchen: ₹.5 Lakh
\n* Wardrobe: ₹.5 Lakh
\n* Other interiors: ₹.2 Lakh
\n_*Specs*: Aquashield, Solid finishes and Tyrox hardware_

\n*COMFORT [Popular] - ₹.6 Lakh*
\n> Perfect for first-time homeowners
\n* Kitchen: ₹.2 Lakh
\n* Wardrobe: $.9 Lakh
\n* Other interiors: ₹.5 Lakh
\n_*Specs*: Hydroguard+, Hi Gloss Finishes and Tyrox hardware_

\n*LUXURY - ₹.7 Lakh*
\n> Best of design and style
\n* Kitchen: ₹.5 Lakh
\n* Wardrobe: ₹.3 Lakh
\n* Other interiors: ₹.8 Lakh
\n_*Specs*: BWP ply with Glass/Acrylic/Lacquard finishes and Hettich/Hafele hardware_

\n*Common Kitchen Details*:
\n* Shape: L-shaped
\n* Size: 9ft 1inch x 8ft 3inch

\nNote: This is an approximate estimate based on your selections and may change depending on your space dimensions, design choices, customizations, or additional work requested."""
      
      if size==4:
            return """✨ *Your Interior Design Estimate Summary* ✨

\nWe've prepared 3 lifestyle options for your home:

\n*ESSENTIAL - ₹.4 Lakh*
\n> Ideal for rental properties
\n* Kitchen: ₹.8 Lakh
\n* Wardrobe: ₹.4 Lakh
\n* Other interiors: ₹.2 Lakh
\n_*Specs*: Aquashield, Solid finishes and Tyrox hardware_

\n*COMFORT [Popular] - ₹.0 Lakh*
\n> Perfect for first-time homeowners
\n* Kitchen: ₹.6 Lakh
\n* Wardrobe: ₹.0 Lakh
\n* Other interiors: ₹.5 Lakh
\n_*Specs*: Hydroguard+, Hi Gloss Finishes and Tyrox hardware_

\n*LUXURY - ₹.899999999999999 Lakh*
\n> Best of design and style
\n* Kitchen: ₹.5 Lakh
\n* Wardrobe: ₹.6 Lakh
\n* Other interiors: ₹.8 Lakh
\n_*Specs*: BWP ply with Glass/Acrylic/Lacquard finishes and Hettich/Hafele hardware_

\n*Common Kitchen Details*:
\n* Shape: Parallel
\n* Size: 10ft x 10ft 7inch

\nNote: This is an approximate estimate based on your selections and may change depending on your space dimensions, design choices, customizations, or additional work requested.!"""
      if size==3:
            return  """✨ *Your Interior Design Estimate Summary* ✨

\nWe've prepared 3 lifestyle options for your home:

\n*ESSENTIAL - ₹.0 Lakh*
\n> Ideal for rental properties
\n* Kitchen: ₹.5 Lakh
\n* Wardrobe: ₹.2 Lakh
\n* Other interiors: ₹.2 Lakh
\n_*Specs*: Aquashield, Solid finishes and Tyrox hardware_

\n*COMFORT [Popular] - .6 Lakh*
\n> Perfect for first-time homeowners
\n* Kitchen: ₹.3 Lakh
\n* Wardrobe: ₹.8 Lakh
\n* Other interiors: ₹.5 Lakh
\n_*Specs*: Hydroguard+, Hi Gloss Finishes and Tyrox hardware_

\n*LUXURY - ₹.7 Lakh*
\n> Best of design and style
\n* Kitchen: ₹.5 Lakh
\n* Wardrobe: ₹.4 Lakh
\n* Other interiors: ₹.8 Lakh
\n_*Specs*: BWP ply with Glass/Acrylic/Lacquard finishes and Hettich/Hafele hardware_

\n*Common Kitchen Details*:
\n* Shape: L-shaped
\n* Size: 9ft 5inch x 8ft 3inch

\nNote: This is an approximate estimate based on your selections and may change depending on your space dimensions, design choices, customizations, or additional work requested."""
      else:
            return "Due to the grand scale of your project, calculating an exact estimate instantly can be a bit complex. Why don't we book a complimentary consultation call instead? This will allow us to understand your complete requirements in detail and provide you with a perfectly tailored cost breakdown. ✨"

 except Exception as e:
      return "sorry i am unable to calculate your budget write now "