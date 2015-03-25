# Stack implemented using linked list
from node import *

class Stack:
	def __init__(self):
		self.head= None
	def push(self,item):
		temp= Node(item)
		if self.head == None:
			self.head = temp
		else:
			temp.setNext(self.head)
			self.head= temp
	def pop(self):
		a= self.head
		b= self.head.getNext()
		self.head= b
		return a.getData()
	def peek(self):
		return self.head.getData()
	def isEmpty(self):
		return self.head== None
	def size(self):
		current = self.head
		counter=0
		while current != None:
			current = current.getNext()
			counter += 1
		return counter

a= Stack()
a.push(5)
a.push(6)
a.push(3)
# 3
print a.pop() 
# 6
print a.peek()
# False
print a.isEmpty()
# 2
print a.size()


