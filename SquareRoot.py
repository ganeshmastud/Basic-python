print("finding square root")
class square():
	def __init__(self,num):
		self.num=num
	def cal_square(self):	
  		return (self.num*self.num)

x=int(input("Enter the number:"))
obj=square(x)
print("The square root of",x,"is",obj.cal_square())
print()