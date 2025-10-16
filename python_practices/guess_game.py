import random
secret_num = random.randint(1,10)
cho = 'y'
print("I am thinking of a number between 1 and 10. can u gusee it?")
while(cho == 'y'):
 for i in range(3):
    guess = int(input(f"You have {3 - i} trial(s): "))
    if secret_num == guess:
        print("Congratulations, you guessed it!")
        break
    elif secret_num < guess:
        print("Nope, your guess is a bit high. Give it another shot!")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")
    
 cho = input("do you want to contnue?(y/n)")