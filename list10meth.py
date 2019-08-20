try:
  i=int(input("Enter the 1 if you want to continue otherwise press zero."))
  while i>0:
    list=[1,2,'cat',45,'dog',57,68 ,-5,'man',574,'girl']
    print(list)
    print("We are doing 10 different method on the list.")
    print("1.append()\t2.insert()\t3.extend()\n4.cunt()\t5.index()\t6.pop()\n7.remove()\t8.delete\t9.reverse()\n10.length()")
    ch=int(input("Enter your choice:"))

    if ch==1:
      #method 1
      p=input("Enter the element to list:")
      list.append(p) #this method adds the value at end of the list
      print(list)


    elif ch==2:
      #method 2 - insert(): element at specified position.
      p=int(input("Enter the location:"))
      x=input("Enter the data:")
      list.insert(p,x)#inserting at 2nd postion.
      print(list)

    elif ch==3:
      #method 3-extend()
      print("Enter the integer values:")
      list2=[int(x) for x in input().split()]
      print(list2)
      print("This is extended list")
      list.extend(list2)#adding the content of 2nd lsit to the 1st list
      print(list)


    elif ch==4:
    #method 4-count()
      print("If you want to count string press 1 or integer value press 2")
      ch=input("Enter the choice:")
      if(ch==1):
        p=input("Enter the element to be counted by prog : ")
      else:
         p=int(input("Enter the element to be counted by prog : "))
      print(list.count(p))#count the no of time element arrives in the list


    elif ch==5:
      #method 5-index()
      p=input("Enter the element two get the position:")
      print("position of element:",list.index(p))#gives the position of element


    elif ch==6:
      #method 6-pop(): Index is not a necessary parameter, if not mentioned takes the last index.
      p=input("Enter the element to be pop otherwise it will pop last element form the lsit:")
      print("deleting the element:",list.pop(4))#4th element is deleted.
      print("After deleting the 4 element:\n",list)


    elif ch==7:
      #method 7-remove()Element to be deleted is mentioned using list name and element.
      p=input("Enter the element to remove:")
      list.remove(p)
      print("After removing",p,"from the list:\n",list)



    elif ch==8:
      #method 8-del() : Element to be deleted is mentioned using list name and index.
      p=int(input("Enter the index location of the element:"))
      del list[p]
      print("After deleting the",p," element list is:\n",list)




    elif ch==9:
      #method 9-reverse()
      list.reverse()
      print("Reverse list is:\n",list)



    elif ch==10:
      #method 10-length()
      print("The length of the list is:",len(list))
    else:
      break
except ValueError:
  print("Enter the integer value.")
except IndexError:
  print("The index u entered is out of the range of the lsit.")
except SyntaxError:
  print("Invalid syntax.")
except TypeError:
  print("for the userdefined list you can store only integer value.")