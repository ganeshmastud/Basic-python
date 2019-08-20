try:
  print("Enter the space betw value in the list:" )
  l=[int(x) for x in input().split()]
  z=int(input("Enter value to search:"))
  print("position is:",l.index(z))
except ValueError:
  print("The",z,"is not in list")