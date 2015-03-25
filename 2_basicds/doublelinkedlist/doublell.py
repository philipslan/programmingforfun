# implement doubly-linked list
from node import *

class List:
	def __init__(self):
		self.head= None
		self.tail= None
	def add(self,item):
		new= Node(item)
		if self.head== None:
			self.head= new
			self.tail= new
		else:
			new.setNext(self.head)
			self.head.setPrevious(new)
			self.head= new
	def remove(self,item):
		current= self.head
		found = False
		while (current != None) and (not found):
			if current.getData() == item:
				found = True
			else:
				current= current.getNext()
		if found:
			if current.getPrevious() != None:
				current.getPrevious().setNext(current.getNext())
			if current.getNext() != None:
				current.getNext().setPrevious(current.getPrevious())
	def search(self,item):
		current= self.head
		found = False
		while (current != None) and (not found):
			if current.getData() == item:
				found = True
			else:
				current= current.getNext()
		return found
	def isEmpty(self):
		return self.head== None
	def size(self):
		count= 0
		current= self.head
		while current != None:
			count += 1
			current = current.getNext()
		return count
	def append(self,item):
		a= Node(item)
		self.tail.setNext(a)
		a.setPrevious(self.tail)
		self.tail= a
	def index(self,item):
		current= self.head
		found = False
		pos=0
		while (current != None) and (not found):
			if current.getData() == item:
				found = True
			else:
				current= current.getNext()
				pos += 1
		return pos
	def insert(self,pos,item):
		new= Node(item)
		current= self.head
		count= 0
		found= False
		while current != None and (not found):
			if count == pos:
				found= True
			else:
				count += 1
				current= current.getNext()
		if found:
			current.getPrevious().setNext(new)
			new.setPrevious(current.getPrevious())
			current.setPrevious(new)
			new.setNext(current)
	def pop(self):
		a= self.tail
		a.getPrevious().setNext(None)
		self.tail= a.getPrevious()
		return a.getData()
	def popp(self,pos):
		current= self.head
		count= 0
		found= False
		while current != None and (not found):
			if count == pos:
				found= True
			else:
				count += 1
				current= current.getNext()
		if found:
			if current.getPrevious() != None:
				current.getPrevious().setNext(current.getNext())
			if current.getNext() != None:
				current.getNext().setPrevious(current.getPrevious())
			return current.getData()
		else:
			return None


a= List()
a.add(5)
a.add(3)
a.append(4)
a.append(6)
a.insert(2,10)
a.remove(4)
print a.search(5)
print a.size()
print a.index(10)
print a.pop()
print a.popp(2)

