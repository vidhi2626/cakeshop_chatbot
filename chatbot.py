from os import truncate
rules = {
    # 1. Greetings and Basic Chat
    "hello": "Welcome to the Happy Cake Shop! How can I help you today?",
    "hi": "Welcome to the Happy Cake Shop! How can I help you today?",
    "kem chho": "Welcome to the Happy Cake Shop! Majama! How can I help you today?",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "bye": "Thank you for visiting! We hope to see you again soon.",
    "aavjo": "Thank you for visiting! We hope to see you again soon.",

    # 2. Information about the Shop
    "menu": "We have Chocolate Truffle, Red Velvet, Pineapple Cream, and Black Forest cakes. You can also ask me to 'recommend' a cake!",
    "location": "We are located at 150 Feet Ring Road, Rajkot.",
    "address": "We are located at 150 Feet Ring Road, Rajkot.",
    "timings": "We are open from 10:00 AM to 9:00 PM every day.",
    "open": "We are open from 10:00 AM to 9:00 PM every day.",
    
    # 3. Details about Specific Cakes
    "chocolate cake": "Our Chocolate Truffle cake is a rich, decadent classic. It costs ₹600.",
    "truffle cake": "Our Chocolate Truffle cake is a rich, decadent classic. It costs ₹600.",
    "red velvet": "Our Red Velvet with cream cheese frosting is a customer favorite! It costs ₹750.",
    "pineapple cake": "A light and fruity choice! Our Pineapple Cream cake is ₹550.",

    # 4. Keywords to Trigger Engaging Features
    "recommend": "I'd love to help! What is the occasion? (e.g., 'birthday', 'anniversary', 'party')",
    "suggest": "I'd love to help! What is the occasion? (e.g., 'birthday', 'anniversary', 'party')",
    "custom": "Let's build your perfect cake! We can start with the flavor, shape, and a special message.",
    "build": "Let's build your perfect cake! We can start with the flavor, shape, and a special message."
}
def cakeshop():
  print("welcome to Cakeshop")
  while True:
    user_input=input("you:").lower()
    responce_found = False
    
    for key in rules:
      if key in user_input:
        print(f">Bot : {rules[key]}")
        responce_found = True
    
    '''  if "price of blackforest" in user_input:
      print("The price of this item is $4600")
    elif "bill" in user_input:
      print("your bill is $5000")'''

    if "bye" in user_input:
      print("Have a good day!")
      break

    if responce_found == False:
      print(">Bot : i didn't understand this")
    
cakeshop()
