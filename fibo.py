print("----Fibonnaci series----")
def fibo(x):
  if x<0:
    return 1
  elif x<=1:
    return 1
  else:
    return (fibo(x-1)+fibo(x-2))
x=int(input("Enter the number:"))
for i in range(x+1):
    print("the fibonacci series  for ",i,":",fibo(i))

