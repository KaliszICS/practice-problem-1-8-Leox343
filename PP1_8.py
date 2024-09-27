'''
  lesson 1.7
  created on sept 26
  created by Leo Xu
  last edited on sept 27
'''
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  #Write Assignment code here
  bool = input("Enter an integer: ")
  bool = int(bool) != 0 
  print(bool)
def q3():
  #Write Assignment code here
  bool3 = input("Enter a number: ")
  print((float(bool3) >= 0.0) and (float(bool3) <= 10.0))
def q4():
  #Write Assignment code here
  bool4 = input("Input food: ")
  bool5 = input("Input drink: ")
  bool4 = bool4 == "pizza"
  bool5 = bool5 == "pop"
  print(not(bool4 and bool5))
def q5():
  #Write Assignment code here
  bool6 = input("Enter an integer: ")
  bool7 = int(bool6) % 2 == 0
  print(f"The integer {bool6} is {bool7}.")
#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
