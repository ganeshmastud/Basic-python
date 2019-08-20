while True:
	x,y=(int(x) for x in input("Enter two number and make sapce after each number that you enter :").split())
	print("Enter the operation no:1.add\t2.sub\t3.mul\t4.div")
	z=int(input("Enter the number for opn:"))
	if(z==1):
		print("sum =",x+y)
	elif(z==2):
		print("sub=",x-y)
	elif(z==3):
		print("Mul =",x*y)
	elif(z==4):
	  print("Modulo =",x%y)
	  print("div =",x/y)
	else:
	  print("Enter the rigth operation.")
	  exit()
	