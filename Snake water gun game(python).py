import random

a=['s','w','g']

p=0
NOC=10
HA=0
CA=0
print('s for snake w for water g for gun \n')
while p<NOC:
    com=str(input())
    my=random.choice(a)
    print(my)


    if (com==my):
        print("game draw")

    elif(com=="s" and my=="w"):
        print("i win the game")
        HA = HA + 1
    elif (com== "s" and my== "g"):
        print("computer wins the game")
        CA = CA + 1
    elif (com== "w" and my== "s"):
        print("computer wins the game")
        CA=CA+1
    elif (com== "w" and my == "g"):
        print("i win the game")
        HA=HA+1
    elif (com== "g" and my== "s"):
        print("i win the game")
        HA=HA+1
    elif (com== "g" and my == "w"):
        print("computer wins the game")
        CA=CA+1

    p=p+1

print("game over")
print("my score",HA)
print("computer score",CA)

if(HA>CA):
    print("congrats you win the game")
elif(HA<CA):
    print("congrats computer win the game")