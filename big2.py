# Implement Big 2
import random

class Card:
	def __init__(self,number,suit):
		self.number= number
		self.suit= suit

	def getNumber(self):
		return self.number

	def getSuit(self):
		return self.suit

class Deck:
	def __init__(self):
		suits=["hearts","diamonds","spades","clubs"]
		values= ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
		self.deck=[]
		for suit in suits:
			for value in values:
				card= Card(value,suit)
				self.deck.append(card)
	def getDeck(self):
		return self.deck
	def getTopCard(self):
		return self.deck[0]
	def shuffleDeck(self):
		new=[0]*52
		shuffled=0
		while shuffled==0:
			if (0 in new) == False:
				shuffled=1
			else:
				for item in range(len(new)):
					new[item]= 2
		self.deck= new
		return self.deck



a=Deck()
print a.getTopCard().getSuit()
print a.getTopCard().getNumber()
print a.shuffleDeck()

		

