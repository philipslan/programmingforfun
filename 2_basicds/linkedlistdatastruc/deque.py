from node import *
# deque using linked list
class Deque:
	def __init__(self):
		self.head= None
	def addFront(self,item):
		new= Node(item)
		if self.head==None:
			self.head= new
		else:
			new.setNext(self.head)
			self.head= new
	def addRear(self,item):
		new = Node(item)
		if self.head== None:
			self.head= new
		else:
			current= self.head
			while current.getNext() != None:
				current = current.getNext()
			current.setNext(new)
	def removeFront(self):
		a=self.head
		if a== None:
			return None
		else:
			self.head= a.getNext()
			return a.getData()
	def removeRear(self):
		current= self.head
		if current == None:
			return None
		else:
			while current.getNext() != None:
				previous= current
				current= current.getNext()
			previous.setNext(None)
			return current.getData()
	def isEmpty(self):
		return self.head==None
	def size(self):
		count= 0
		current= self.head
		while current != None:
			count += 1
			current = current.getNext()
		return count

a= Deque()
a.addFront(5)
a.addFront(3)
a.addFront(13)
a.addFront(17)
a.addFront(4)
print a.removeRear()
print a.removeFront()
print a.isEmpty()
print a.size()

