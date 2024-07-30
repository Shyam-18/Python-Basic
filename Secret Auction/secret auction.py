from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
dictionary = {}
user = "yes"
while user == "yes":
  name = input("Enter your name: ")
  bid = int(input("Enter your bid amount: $"))
  dictionary[name] = bid
  user = input("Are there any other users who bid, Enter 'yes' or 'no':")
  if user == "yes":
    clear()
max = 0
nam = ""
for name in dictionary:
  if dictionary[name] > max:
    max = dictionary[name]
    nam = name

print(f"{nam} won as he bidded the highest amount: ${max}")
  