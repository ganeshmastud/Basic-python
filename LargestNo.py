while True:
	try:
		x,y,z=(int(x) for x in input("Enter three numbers and make sapce after each number that you enter:").split())
		if x>y and x>z:
		   print("Largest value is {}x}:",x)
		elif y>x and y>z:
		   print("Largest value is{y}:",y)
		elif z>x and z>y:
		   print("Largest value is{z}:",z)
	except ValueError:
		print("Enter only the integer value and make space after each value.")
	  