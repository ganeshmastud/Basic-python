s=input("Enter the string:")
print(s)
words=s.split()
print(words)
words.sort()
print("The sorted words are:")
for word in words:
  print(word,end=",")
