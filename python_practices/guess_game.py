import random
secret_num = random.randint(1,100)
cho = 'y'
print("I am thinking of a number between 1 and 10. can u gusee it?")
while(cho == 'y'):
 for i in range(10):
    guess = int(input(f"You have {10 - i} trial(s): "))
    if secret_num == guess:
        print("Congratulations, you guessed it!")
        break
    elif secret_num < guess:
        print("Nope, your guess is a bit high. Give it another shot!")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")
 else:
    print(f"sorry, the numbere was {secret_num}")
 cho = input("do you want to contnue?(y/n)").lower()
 if cho == 'y':
    secret_num = random.randint(1,100)

