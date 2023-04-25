def check(string):
  upper, lower = 0,0
  for i in string:
    if i.isupper():
      upper+=1
    elif i.islower():
      lower+=1
    
  print("Uppercase =",upper,"lowercase =",lower,)

check("HeLLo")