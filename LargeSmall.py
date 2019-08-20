print("Enter the data to list:")
l=[int(x) for x in input().split()]
print(l)
small=l[0]
large=l[0]
for i in range(0,len(l)):
  if(l[i]<small):
    small=l[i]
  else:
    large=l[i]
print("The smallest number is:",small)
print("The lagrest number is:",large)