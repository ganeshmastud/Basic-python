while True:
	def dist(d1,d2):
	  td=d1+d2
	  return td
	d1=float(input("Enter the distance for d1:"))
	print("The distance is:",d1)
	d2=float(input("Enter the distance for d2:"))
	print("The disance is:",d2)

	#td=1
	td=dist(d1,d2)
	print("The total distance is:",td)


	print("1.for meter to feet\n2.feet to inches.")
	while True:
		x=int(input("choose the operation:"))
		feet=td*3.281
		inches=feet*12
		if x==1:
		  print("the distace in feet is:",feet)
		elif x==2:
		  print("the feet in inches is:",inches)
		else:
		  print("Enter the right choce.")
