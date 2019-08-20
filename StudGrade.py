x=int(input("Enter your Enrollment no:"))
marks=int(input("Enter your marks to get grades:"))
if marks>=91 and marks<=100:
  print(x,"You got A+ grade.Congratulation your first")
elif marks >=81 and marks <=90:
   print(x,"You got A grade.")
elif marks>=71 and marks <=80:
   print(x,"You got B+ grade.")
elif marks >=61 and marks <=70:
   print(x,"You got B grade.")
elif marks >=51 and marks <=60:
  print(x,"You got C+ grade, you have to work hard.")
elif marks >=41 and marks <=50:
  print(x,"You got C grade, you have to work hard.")
elif marks >=40:
  print(x,"You are fail , try next sem.")
else:
  print ("Marks sholud be less than hundred.")
