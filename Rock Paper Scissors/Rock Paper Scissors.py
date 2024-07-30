import random

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

user_number = int(
    input("choose one, Type 0 for Rock,1 for paper,2 for scissors.\n"))
if (user_number == 0):
  print(rock)
elif (user_number == 1):
  print(paper)
elif (user_number == 2):
  print(scissors)

computer_number = random.randint(0, 2)
print("Computer chose:\n")
if (computer_number == 0):
  print(rock)
elif (computer_number == 1):
  print(paper)
elif (computer_number == 2):
  print(scissors)
if (user_number == 0 and computer_number == 1):
  print("You Lose")
elif (user_number == 0 and computer_number == 2):
  print("You Win")
elif (user_number == 1 and computer_number == 0):
  print("You Win")
elif (user_number == 1 and computer_number == 2):
  print("You Lose")
elif (user_number == 2 and computer_number == 0):
  print("You Lose")
elif (user_number == 2 and computer_number == 1):
  print("You Win")
elif (user_number == 0 and computer_number == 0):
  print("Its a Draw")
elif (user_number == 1 and computer_number == 1):
  print("Its a Draw")
elif (user_number == 2 and computer_number == 2):
  print("Its a Draw")
else:
  print("Invalid number results in a lose")
