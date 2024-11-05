import random


user=int(input("enter the number between1 to 6:"))
ran_num=random.randint(1,user)
if user==ran_num:
    print(f"you win your guess {user} and the random num is {ran_num} matched")
else:
    print(f"you lose your guess {user} and the random num  {ran_num}is not matched ")