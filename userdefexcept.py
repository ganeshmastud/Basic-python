class Myexception(Exception):
  def __init__(self, arg):
    self.msg=arg
def check(dict):
  for user,attendance in dict.items():
    print('name={:15s} attendance={:10.2f}'.format(user,attendance))
    if(attendance<55.0):
      raise Myexception("you have really low attendance "+user)
class1 ={'raj':70.00, 'vani':50.30, 'Ajay':60.50, 'Naresh':20.40}
try:
  check(class1)
except Myexception as me:
  print(me)