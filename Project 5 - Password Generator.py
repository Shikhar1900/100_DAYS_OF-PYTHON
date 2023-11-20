#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#generating the letters:
Password = ""
for letter in range (1, nr_letters + 1):
    Index_Letter = random.randint(0, nr_letters)
    Pass_Letter = letters [Index_Letter]
    Password += Pass_Letter

for symbol in range (1, nr_symbols + 1):
    Index_Symbol = random.randint(0, nr_symbols)
    Pass_Symbol = symbols [Index_Symbol]
    Password += Pass_Symbol

for number in range (1, nr_numbers + 1):
    Index_Number = random.randint(0,nr_numbers)
    Pass_Number = numbers [Index_Number]
    Password += Pass_Number


print (Password)
New_Password = ""
for Pass in range (0,len(Password)+1):
    Index = random.randint (0, len(Password)-1)
    J_Pass = Password [Index]
    New_Password += J_Pass

print (New_Password)