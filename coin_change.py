# Small coin program, pretty simple, part of my Discrete Math practice thingy

def coin_change(coins: int) -> set:
	change: dict = {
	"quarters": 0,
	"dimes": 0,
	"nickels": 0,
	"pennies": 0
	}

	while coins > 0:
		print(coins)
		if coins//25 > 0:
			change["quarters"] += coins//25
			coins -= coins//25 * 25

		elif coins//10 > 0:
			change["dimes"] += coins//10
			coins -= coins//10 * 10

		elif coins//5 > 0:
			change["nickels"] += coins//5
			coins -= coins//5 * 5

		elif coins//1 > 0:
			change["pennies"] += coins//1
			coins -= coins//1

	return change
