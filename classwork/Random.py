import random

chance = 0
game= random.randint(0,100)
print("READY FOR THE GAME")
while chance < 3:
    number: int = int(input("Enter number: "))
    if (number > game):
        print("Number is too high")
    elif (number < game):
        print("Number is too low")
    chance+=1
else:
    print()
    print("Game lost")

