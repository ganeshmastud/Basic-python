print("---Calculate library fine---")
def calLibraryFine( cat , noOfDays , bookLost):
	totalCost = 0
	if cat =="eng":
		totalCost +=(noOfDays - 15) * 2
		if (bookLost=="yes"):
			totalCost += 1000
		else:
			pass
	elif cat == "mgmt":
		totalCost += (noOfDays - 15) * 3
		if (bookLost=="yes"):
			totalCost += 1000
		else:
			pass
			
	else:
		print("Enter the right value.")
	print(totalCost)	
	print("The {0} book has {1} rupee cost".format(cat,str(totalCost)) )
x=input("Enter Category 1.eng ,2.mgmt:")
y=int(input("Enter the no. of days for book you kept:"))
z=input("book lost yes or no: ")
calLibraryFine(x,y,z)
