def word_count(str):
  count=0
  words=str.split()
  for i in words:
      print(i)
      count +=1
  print("The count of word is:",count)
  print("The count of blank space is:",count-1)
  
str=input("Enter the string:")
print(word_count(str))
