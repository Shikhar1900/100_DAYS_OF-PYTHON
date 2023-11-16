rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#Import the random variable to generate the a random number to co-relate, as the machine's response.
import random
Combined_Actions = [rock, paper, scissors]
Machine_Action = random.randint(0,2)

Human_Action = int(input ("Please choose an action: Choose 0 for Rock, 1 for Paper and 2 for Scissors. : "))

print (f"You chose: \n {Combined_Actions[Human_Action]}")

print (f"The Computer chose: \n {Combined_Actions[Machine_Action]}")



# Testing the random function:
# print (Machine_Action)

if Human_Action == Machine_Action:
    print ("It is a draw!")

elif  Human_Action == 0 and Machine_Action == 2:
    print ("You have won the game!") 

elif Human_Action > Machine_Action:
    print ("Congratulations! You have won!")

else:
    print ("Sorry.You have lost the game.")