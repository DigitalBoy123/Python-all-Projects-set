import random
n = random.randint(1,100)
guess =0
a =  -1
while(a != n):
    guess +=1
    a = int(input("Enter your guess: "))
    if(a > n):

        print("Please! lower number")
    else:
        print("Please! Highter number")

print(f"You have guessed the {n} correct number in {guess} attempts")
        
        
     
    