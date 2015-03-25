# Overall superclass
class LogicGate:
	def __init__(self,n):
		self.label= n
		self.output= None
	def getLabel(self):
		return self.label
	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

# Super class for AndGate and OrGate
class BinaryGate(LogicGate):
	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pinA= None
		self.pinB= None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate" + self.getLabel()+"-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate" + self.getLabel()+"-->"))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RuntimeError("Error: NO EMPTY PINS")


# Super class for NotGate
class UnaryGate(LogicGate):
	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pin=None

	def getPin(self):
		if self.pin==None:
			return int(input("Enter Pin input for gate"+ self.getLabel()+"-->"))
		else:
			return self.pin.getFrom().getOutput()
	def setNextPin(self,source):
		if self.pin == None:
			self.pin = source
		else:
			print("Cannot Connect: NO EMPTY PINS on this gate")

# AndGate IS-A BinaryGate. If both pins are not 1 then it returns 0.
class AndGate(BinaryGate):
	def __init__(self,n):
		BinaryGate.__init__(self,n)
	def performGateLogic(self):
		a= self.getPinA()
		b= self.getPinB()

		if a==1 and b==1:
			return 1
		else:
			return 0

# OrGate IS-A BinaryGate. If at least one of the pins is a 1 it returns 0.
class OrGate(BinaryGate):
	def __init__(self,n):
		BinaryGate.__init__(self,n)
	def performGateLogic(self):
		a= self.getPinA()
		b= self.getPinB()
		if a==1 or b==1:
			return 1
		else:
			return 0

# NotGate IS-A UnaryGate. It returns 0 if the pin is 1 and 1 if the pin is 0.
class NotGate(UnaryGate):
	def __init__(self,n):
		UnaryGate.__init__(self,n)
	def performGateLogic(self):
		a= self.getPin()
		if a==1:
			return 0
		else:
			return 1

# Connector HAS-A LogicGate
class Connector:
	def __init__(self,fgate,tgate):
		self.fromgate=fgate
		self.togate=tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate
	def getTo(self):
		return self.togate

class NorGate(OrGate):
	def __init__(self,n):
		OrGate.__init__(self,n)
	def performGateLogic(self):
		a= OrGate.performGateLogic(self)
		if a= 1:
			return 0
		else:
			return 1

class NandGate(AndGate):
	def __init__(self,n):
		AndGate.__init__(self,n)
	def performGateLogic(self):
		a= AndGate.performGateLogic(self)
		if a ==1:
			return 0
		else:
			return 1

