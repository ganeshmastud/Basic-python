count=0
print("Printing the Even nos betw 1 to 100.")
for i in range (100+1):
  if(i%2==0):
    count +=1
    print(i,end=' ')
  else:
    pass
print("\nThe count of even number is:",count)