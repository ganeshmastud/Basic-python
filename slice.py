lst=['this', 1,2.34,'is','my','first program','in','python','prog','lang'] # we can also use slice function on tuples but in here we use list
print(lst)
lst1=[23,43,5,456,56,7]
print(lst1)
print("\n\n\n1.valAtPos\t2.last Loc\t3.from the given loc to the last\n4.show val betw to pos giv by user\n5.show val betw to pos giv by user by avoiding two pos val\n6.assign neg val\n7.exit")
while True:
	
	
	ch=int(input("Enter your choice:"))
	if ch==1:
		p=int(input("Enter the pos:"))
		print(lst[p]) # showing the value at given position
	elif ch==2:
		print("lst[-1]")
		print(lst[-1]) #showing the vlue at last position
	elif ch==3:
		print("lst[5:]")
		print(lst[5:]) #printing the value form five onwords till the end of list.
	elif ch==4:
		print("lst[3:7]")
		print(lst[3:7])# printing the value from 3 to 6.

	elif ch==5:
		print("lst1[2:7:2]")
		print(lst1[2:7:2])#this is the complete slicing ex. we start at pos 2 til pos end-1 and step by 2
	elif ch==6:
		print("lst1[-1:-5:-2]")
		print(lst1[-1:-5:-2])# here we assing negative value. 
	elif ch==7:
		exit()
	else:
		print("Wrong choice.")
		
