# two functions that have separate speeds
import time

def comparensquared(array):
	start= time.time()
	minimum=0
	for item in array:
		for item1 in array:
			if item < item1:
				minimum= item
			else:
				pass
	end= time.time()
	total= end-start
	return [minimum,total]

def comparen(array):
	start= time.time()
	minimum= array[0]
	for item in array:
		if minimum < item:
			pass
		else:
			minimum= item 
	end= time.time()
	total= end-start
	return [minimum,total]

a= list(range(10000))
a= a[::-1]

print comparensquared(a)
print comparen(a)