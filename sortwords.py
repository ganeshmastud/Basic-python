str=input("Enter the string:")
words=str.split()
words.sort()
print("The sorted words are:\n")
for word in words:
	print(word)