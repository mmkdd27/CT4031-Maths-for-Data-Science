#1
print("Hello, world!")
age = 45
print("You have", 65 - age, "years until retirement")

#2
age = input("How old are you? ")
print ("Your age is", age)
print ("You have", 65 - int(age), "years until retirement")

#3
Grade = 34
if Grade > 39:
    print ("You have passed.")
else:
    print("You have failed.")

#4
Grade = 34
if Grade > 39:
    print ("You have passed.")
elif Grade > 0:
    print ("You have to do a reassessment.")
else:
    print("You have failed.")

#5
for x in range(1, 6):
    print (x, "squared is", x * x)

#6
sum = 0
for i in range(1, 11):
    sum = sum + (i * i)
print ("sum of first 10 squares is", sum)
