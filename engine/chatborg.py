import sys
sys.path.insert(0, './engine/lib/')
import starter_convo
import random, secrets


def chooseChatBot(chatbot):
	
	if chatbot.lower() == "john":
		chat_Bot = MainChatbot('John')
	
	elif chatbot.lower() == "tim":
		chat_Bot = CasualChatbot('Tim')
	
	elif chatbot.lower() == "suzie":
		chat_Bot = FormalChatbot('Suzie')

	else: 
		print("Too bad, you're gonna talk to John now.")
		chat_Bot = MainChatbot('John')

	return chat_Bot




class MainChatbot:

	def __init__(self, name):		
		self.name = name

	def greeting(self, user):
		greetings = starter_convo.starter['greetings']['casual_greetings']+starter_convo.starter['greetings']['formal_greetings']
		return secrets.choice(greetings)+" "+user

	def __repr__(self):
		return "Hi my name is "+ self.name +" Let's Chat :)"


# ----------------- CasualChatbot ------------------
class CasualChatbot(MainChatbot):
	def greeting(self, user):
		return secrets.choice(starter_convo.starter['greetings']['casual_greetings'])+" "+user



# ----------------- FormalChatbot ------------------
class FormalChatbot(MainChatbot):
	def greeting(self, user):
		return secrets.choice(starter_convo.starter['greetings']['formal_greetings'])+" "+user