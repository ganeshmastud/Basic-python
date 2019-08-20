punctuation='''!@#$%^&*()_{}[]:"<>?/|\_-+=~`";:""'',.'''
str=input("Enter the string:\n")
no_punc=""
for char in str:
  if char not in punctuation:
    no_punc=no_punc + char
print(no_punc)
