class add():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		return self.a+self.b
	def sub(self):
		return self.a-self.b
	def mul(self):
		return self.a*self.b
	def div(self):
		return self.a%self.b
try:
	print("---calculator---")
	print("1.add\t2.sub\t3.mul\t4.div\t5.exit")
	while True:
		x=int(input("Enter the no:"))
		y=int(input("Enter the no:"))
		obj=add(x,y)
		ch=int(input("Enter your choice:"))
		if ch==1:
			print("addition is:"obj.add())
		elif ch==2:
			print("Subtraction is:"obj.sub())
		elif ch==3:
			print("Multiplication is:"obj.mul())
		elif ch==4:
			print("Division is:"obj.div())
		elif ch==5:
			exit()
		else:
			print("Wrong opn enterd,pls enter right opn")
		
except ValueError:
	print("Enterd integer value.")	