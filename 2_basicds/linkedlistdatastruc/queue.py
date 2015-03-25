# Queue implemented using linked list
from node import *

class Queue:
	def __init__(self):
		self.head= None
	def enqueue(self,item):
		a= Node(item)
		if self.head== None:
			self.head= a
		else:
			a.setNext(self.head)
			self.head= a
	def dequeue(self):
		a= self.head
		if a== None:
			pass
		else:
			while a.getNext() != None:
				previous= a
				a= a.getNext()
			previous.setNext(None)
			return a.getData()
	def isEmpty(self):
		return self.head==None
	def size(self):
		temp = self.head
		count=0
		if temp == None:
			pass
		else:
			while temp.getNext() != None:
				count +=1
				temp= temp.getNext()
		return count


a= Queue()
a.enqueue(5)
a.enqueue(6)
a.enqueue(7)
a.enqueue(8)
a.enqueue(9)
print a.dequeue()
print a.dequeue()
print a.dequeue()
print a.dequeue()
print a.isEmpty()
print a.size()


