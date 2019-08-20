while True:
	n=int(input("Enter a number:"))
	tot=0
	while(n>0):
		dig=n%10
		tot=tot+dig
		n=n//10
	print("The total sum of digits is:",tot)
	print("To stop the prog press ctrl and c")

"""num=int(input("Enter the no:"))
res=0
hold=num
while num>0:
  rem=num%10
  res= res +rem
  num=int(num/10) 
print("The sum of digits is:",res)"""
