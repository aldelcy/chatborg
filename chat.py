import sys
sys.path.insert(0, 'engine/')
import chatborg

# Start by asking user his/her name
user = input("Hi, what is your name? >> ")

# Ask who they want to talk to
chatbot = input("""Who would you like to chat with? 
(John, Tim or Suzie?)
>> """)

# Create chatbot
chat_bot = chatborg.chooseChatBot(chatbot)

# Start convo
print( chat_bot.greeting(user) )