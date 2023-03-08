#!/usr/bin/python3
for x in range(100):
	if int(x / 10) != x % 10 and int(x / 10) < x % 10:
		print("{}{}".format(int(x / 10), x % 10), end="")
		if (x != 89):
			print(", ", end="")
print("")
