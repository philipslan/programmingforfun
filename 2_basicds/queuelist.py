# Implement the Queue ADT, using a list such that the rear of the queue
# is at the end of the list. 
class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)
		print self.items

	def dequeue(self):
		a= self.items[0]
		del self.items[0]
		print self.items
		return a

	def size(self):
		return len(self.items)

queue= Queue()
queue.enqueue(4)
queue.enqueue(7)
queue.enqueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print queue.dequeue()
print queue.isEmpty()