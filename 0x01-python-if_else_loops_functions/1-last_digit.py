#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
	lastnum = (-number % 10) * -1
else:
	lastnum = number % 10

info = f"Last digit of {number} is {lastnum}"

if lastnum > 5:
	print(f"{info} and is greater than 5")
elif lastnum == 0:
	print(f"{info} and is 0")
else:
	print(f"{info} and is less than 6 and not 0")
