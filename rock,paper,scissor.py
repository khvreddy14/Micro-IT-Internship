import random


you = int(input("enter 0 for rock,1 for paper,2 for scissors:"))
if you == 0:
  print("your choice is:rock")
elif you == 1:
  print("your choice is:paper")
elif you == 2:
  print("your choice is:scissors")
else:
  print("")
random = random.randint(0, 2)
if random == 0:
  print("computer choice is:rock")
elif random == 1:
  print("computer choice is:paper") 
else:
  print("computer choice is:scissors")
if you == 0 and random == 1 or you == 1 and random == 2 or you == 2 and random == 0:
  print("computer wins")
elif you == 2 and random == 1 or you == 0 and random == 2 or you == 1 and random == 0:
  print("you won")
elif you == random:
  print("draw")
# else:
#   print("please enter a valid value to play!!")# hence the code executed succesfully
