import string 
import random

#Welcome message for the user and prompts and rules to get them started.

print("Welcome to the Password Generator V1.0.")
print( "A secure password must be at least 8 characters long and contain Digts, Letters and Special Characters!")

# Getting the length of the password for the user

while True:
  try:
    lower_bound = 8
    length = int(input("Please enter the desired length of your password in numbers with a minimum being 8 "))
    if length < lower_bound:
      print("You have entered a number less than",lower_bound, "6creating an insecure password. Please enter a number of 8 or higher to continue.")
      continue
    break
  except ValueError:
    print("Invalid Input.Please try again.")

print("You have choosen",length,"characters.")
print("Lets move onto the next step in creating your strong secure password!")



