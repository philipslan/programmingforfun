# Implement a representation of a Deck
from random import shuffle

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

	def drawCard(self):
		return self.deck[0]

	def shuffleDeck(self):
		shuffle(self.deck)
		return self.deck
		

		

