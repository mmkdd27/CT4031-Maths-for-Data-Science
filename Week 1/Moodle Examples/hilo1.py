import random

points = 0

number1 = random.randint(1, 10)
print("Number is ", number1)

guess = input("H or L?")

number2 = random.randint(1, 10)
print("New Number is ", number2)

if guess=="H" and number2>number1:
    print("RIGHT! Got 10 points")
    points = points + 10
elif guess=="H" and number2<=number1:
    print("WRONG!")
elif guess=="L" and number2<number1:
    print("RIGHT! Got 10 points")
    points = points + 10
elif guess=="L" and number2>=number1:
    print("WRONG!")
else:
    print("?")

print("Points = ", points)
