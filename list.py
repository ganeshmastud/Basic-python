print("1.Enter valuse to list.\n2.display list.\n2.to enter the data at last.\n3.to delete data at position.\n4.to sort the list.\n5.to reverse the list.\6.lenght of the list.\7.copy the lsit.\n8.remove the element from the list.\n9.inserting the data ar loc.")
l=int(input(" enter the numbers to the list:")) ## taking the input from the user.
list=[l]
print("the list 1 is:",list)
l=["stars","in","the","sky"]
print("the 2list is:",l)
print("index:",l.index('in'))
x=int(input("Enter the value for 1 list:"))
list.append(x)  ## It will add the value at the end of the list it dosnt print the value of the list
print("list 1 is is:",list)
print("length of 1 list is:",len(list)) ## to print the lenght of the list we use len keyword
p=int(input("Enter the location to pop from 2 list:"))
print("the pop value is :",l.pop(p))
print("the 2 list is:",l)

l.sort()
print("the sorted 2 list is",l)
print("Count the value:",l.count(5))
l.reverse()
print("the reverse 2list is:",l)
d=str(input("Enter the element to remove."))
l.remove(d)
print ("the remove element is:",d)
print("remove the value at loc:",l)
new_l=l.copy()
new_l.append('gone')
print("the copy list is:",new_l)
v=int(input("Enter the pos."))
b=str(input("Enter the value"))
l.insert(v,b)
print("the list is:",l)

