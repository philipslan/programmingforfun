import random
# Self check 1 and 2 from Problem Solving with Algorithms and Data Structures
# Infinite monkey theorem: a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text
# such as the work of shakespeare.

# 1. Design generate string, stringmatch and callmatch
# 2. Design a progam that improves upon the self check program by keeping letters that are correct and only modifying one character in the best string so far. 
alphabet="abcdefghijklmnopqrstuvwxyz "
# one line of shakespeare
shakespeare= "methinks it is like a weasel"

# genereates random string 
def generatestring():
	string=""
	for x in range(28):
		string += random.choice(alphabet)
	return string

# gives the string a score by comparing it to shakespeare
def stringmatch(string):
	score=0
	for x in range(28):
		if (string[x]==shakespeare[x]):
			score+= 1
	return float(score)/28

def selfcheck(string):
	randomstring=""
	score=0
	string = list(string)
	for x in range(28):
		if string[x]==shakespeare[x]:
			score+= 1
		else:
			string[x]= random.choice(alphabet)
	score= float(score)/28
	string = "".join(string)
	return (score,string)
	

# calls generate string and scores it 100,000,000 times
def callmatch():
	top=0
	topstring=""
	i=0
	string= generatestring()
	while i<1000:
		score= selfcheck(string)
		if score[0]> top:
			top=score[0]
			topstring= score[1]
		if i%10==0:
			print top
			print topstring
		string= score[1]
		i+=1
callmatch()

