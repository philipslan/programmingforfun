# doubly linked list
class Node:
	def __init__(self,data):
		self.previous= None
		self.next=None
		self.data= data
	def getPrevious(self):
		return self.previous
	def getNext(self):
		return self.next
	def getData(self):
		return self.data
	def setPrevious(self,previous):
		self.previous= previous
	def setNext(self,next):
		self.next= next
	def setData(self,data):
		self.data= data




