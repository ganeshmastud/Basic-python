x=input("Enter the String:")
count=0
for i in x:
  if(i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
    print(i,end=' ' )
    count+=1
print("\nThe no of vowels are",count)
