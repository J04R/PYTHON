import random
print("Rock. paper. Scissors")
actions = ["rock", "paper", "scissors"]

user = 0

userpoints = 0
computerpoints = 0


while userpoints < 3 and computerpoints < 3:
  user = input("Your answer: ")
  computer = random.choice(actions)
  print(f"\nYou chose {user}, computer chose {computer}.\n")
  if user == computer:
    print("Tie.")
    print("Computers Score:", computerpoints)
    print("Players Score:", userpoints)
  elif user == "scissors":
    if computer == "paper":
        print("Scissors against Paper. Win.")
        userpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)
    else:
        print("Paper against Rock. Lose.")
        computerpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)
 
  elif user == "rock":
    if computer == "scissors":
        print("Rock against Scissors. Win.")
        userpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)
    else:
        print("Paper against Rock. Lose.")
        computerpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)
  elif user == "paper":
    if computer == "rock":
        print("Paper against Rock. Win.")
        userpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)
    else:
        print("Scissors against Paper. Lose.")
        computerpoints += 1
        print("Computers Score:", computerpoints)
        print("Players Score:", userpoints)

if userpoints == 3:
   print("The player Wins.")
else:
   print("The Computer Wins.")