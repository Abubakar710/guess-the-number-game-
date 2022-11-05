import random
num=random.randint(1,100)
guess_of_number=1
name = input(" please enter the Name ")
print(name)
print("Number of guess is limited is 6 \n Please enter the number ")
while(guess_of_number<=6) :
    guess_number = int(input())
    if guess_number<num:
        print(" You entered number is smaller try again  ")
    elif guess_number>num:
        print(" You entered number is greater try again ")
    elif guess_number==num :
        print(" You won \n")
        print(guess_number)
        break
    print(6-guess_of_number ," Number of guess is left ")
    guess_of_number=guess_of_number+1
if(guess_of_number>6):
    print(" game over, you lost the game \n the correct number is ",num)
