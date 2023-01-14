import random

print("Lets try to guess the number!")

num0 = random.randint(1,100)
print("Try guessing", num0)
state = input("Is the number correct (Yes/No) ?")

while state != "Yes":
	a = input("Is the number higher or lower than correct (High/Low) ?")
	if a == 'High':
		num1 = random.randint()

