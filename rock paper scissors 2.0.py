import random

print("ROCK PAPER SCISSOR GAME")

rock = 0
paper = 1
scissors = 2

print("")
print("rock = 0")
print("paper = 1")
print("scissors = 2")
print("")

chance = 0

a = 0
b = 0
c = 0

while(True):

    opponent = random.randint(0,2)
    you = int(input("Enter your choice from 0 - 2 : "))
        
    if(opponent == you ):
        print("tie")
        chance = chance + 1
        c = c + 1

    if(opponent == 0 and you == 1):
        print("you win")
        chance = chance + 1
        a = a + 1
        break

    if(opponent == 0 and you == 2):
        print("you lose")
        chance = chance + 1
        b = b + 1

    if(opponent == 1 and you == 0):
        print("you lose")
        chance = chance + 1
        b = b + 1

    if(opponent == 1 and you == 2):
        print("you win")
        chance = chance + 1
        a = a + 1
        break

    if(opponent == 2 and you == 0):
        print("you win")
        chance = chance + 1
        a = a + 1
        break

    if(opponent == 2 and you == 1):
        print("you lose")
        chance = chance + 1
        b = b + 1

print("")
print("SCORE BOARD")
print("")
print("your wins :",a)
print("your lose :",b)
print("your ties :",c)
print("")
print("you'v taken",chance,"chances")

