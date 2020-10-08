import random

x=random.randint(1,10)
print("guess the value of x.")
answer=0
while answer!=x:
    answer=eval(input("enter your guess:"))
    if answer > x:
        print("your guess is too high,guess again:")
    elif answer==x:
        print ("YOU got the number:",x)
    else:
        print("your guess is too low,try again:")
