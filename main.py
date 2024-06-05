print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You \'re at a crossroad, where do you want to go? 'Left' or 'Right\n'").lower()

if choice1 == "left":
  choice2 =input("You\ve come to a lake. There is an inland in the middle of the lake. Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n").lower()
  if choice2 == "wait":
    choice3 = input("You\'ve arrived at the Island unharmed. There is a house with 3 doors. One red, one yello and one blue, which colour do you choose?\n").lower()
    if choice3 =="red":
      print("This room is on fire. Game over.\n")
    elif choice3 == "yellow":
       print("You\'ve found the treasure. You\'re a winner!\n")  
    elif choice3 == "blue":
       print("You\'ve entered a room of monsters. Game over.\n")
  else:
    print("You got attacked by shark. Game over.\n")       
else:
    print("You fell into a hole. Game over.\n")