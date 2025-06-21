import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=input("Enter your choise: ")
youDict={"s":1, "w":-1, "g":0}
reverseDict={1:"snake", -1:"water",0:"gun"}
you=youDict[youstr]
print(f"you chose{reverseDict[you]}\n computer chose {reverseDict[computer]}")

if computer==you:
    print("It is a drew")

else:
    if(computer==1 and you==-1):
        print("you lose!")
    elif(computer==0 and you-1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you lose!")
    elif(computer==0 and you==1):
        print("you lose!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==1 and you==0):
        print("you win!")
    else:
        print("Somethig went wrong!")
   
