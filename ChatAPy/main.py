import os
import config
while True:
 
  try:
    print("Welcome to ChatAPy, the simple command line automation system. Made by Emre Arifoglu, please do not remove this welcome message from here ")
    code = input("Code: ")
    value = int(code)
    #Change the code to whatever number you'd like
    #This code will be used in the program, but in order to protect your program, please don't give the code to everyone on the internet, its all up to you! Please make sure to compile the program into an excutable before publishing, to prevent looking at the access code and/or the source code
    if value == config.accesscode:
      print("correct")
      os.system('python chat.py')
    else:
      print("incorrect")
    break;
  except:
    owner = ("Admin")
    print("[", owner ,"]","Im asking for a number, not a letter")

print("Value:", value)
