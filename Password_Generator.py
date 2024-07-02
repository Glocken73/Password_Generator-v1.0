import string 
import random

#Welcome message for the user and prompts and rules to get them started.

print("Welcome to the Password Generator V1.0.")
print( "A secure password must be at least 8 characters long and contain Digits,Letters and Special Characters!")

# Getting the length of the password for the user
# While loop to make sure user chooses at least 9 digits for their password
#while True:
  #try:
    #lower_bound = 8
    #length = int(input("Please enter the desired length of your password in numbers with a minimum being 8 "))
    #if length < lower_bound:
     # print("You have entered a number less than",lower_bound, "6creating an insecure password. Please enter a number of 8 or higher to continue.")
     # continue
   # break
  #except ValueError:
  #  print("Invalid Input.Please try again.")

#print("You have choosen",length,"characters.")
print("Lets move onto the next step in creating your strong secure password!")

# Letting user know which special characters may be selected by the generator


print("Now we must choose the amount of special characters we want in our password.")
print("The special characters are",string.punctuation,)

# While loop to make sure the user selects at least 2 and no more than 8 special characters

while True:
  try:
    special_low = 2
    special_high = 8
    special = int(input("How many special characters would you like in your password? "))
    if special<special_low or special> special_high:
      print("The selection must be",special_low, "or higher and", special_high,"or lower.Please try again.")
      continue
    break
  except ValueError:
    print("Invalid input.Please try again.")

# The users special characters choosen
print("You have choosen", special, "special characters.")

print("Good passwords have a mix of uppercase and lowercase letters.")

while True:
  try:
    upper = list(string.ascii_uppercase)
    upper_low = 2
    upper_high = 6
    upper_choice = int(input("How many upper case letters would you like in your password? "))
    if upper_choice<upper_low or upper_choice>upper_high:
      print("The selection must be", upper_low, "or higher and", upper_high,"or lower. Please choose again. ")
      continue
    break
  except ValueError:
    print("Invalid input. Please try again.")

print("You have choosen",upper_choice,"uppercase letters to be in your password.")
print("We are almost there now.")

print("Finally we should choose the number of lowercase letters to be implemented in our password.")

while True:
  try:
    lower = list(string.ascii_lowercase)
    lower_low = 6
    lower_high = 24
    lower_choice = int(input("How many lower case letters would you like in your password? "))
    if lower_choice<lower_low or lower_choice>lower_high:
      print("The selection must be" ,lower_low,"or higher or", lower_high,"and lower. Please choose again. ")
      continue
    break
  except ValueError:
    print("Invalid input. Please try again.")

print("You have choosen", lower_choice,"lowercase letters to be used in your password.")

number = special+lower_choice+upper_choice

print("Your password will be",number,"characters long. With",special,"special characters,",upper_choice,"uppercase letters and",lower_choice,"lowercase letters!")

  
    
def generate_password(lower_choice, upper_choice, special):
  lower = ''.join(random.choices(string.ascii_lowercase, k=lower_choice))
  upper = ''.join(random.choices(string.ascii_uppercase, k=upper_choice))
  special = ''.join(random.choices(string.punctuation, k=special))

  #combining all the user responses together and shuffling
  all_combo = list(lower+upper+special)
  random.shuffle(all_combo)
  return ''.join(all_combo)

password = generate_password(lower_choice, upper_choice, special)

print("Your generated password is:",password)
