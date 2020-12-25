# I literally can't remember why or how or when I made this... I just founded on coding practice files

def ternary_search(x: int, a:list) -> bool:
	triddle_a: int =  a[len(a)//3]
	triddle_b: int = a[len(a)//3 * 2]

	while len(a) > 1:
		if triddle_a == x or triddle_b == x:
			return True

		if x < triddle_a:
			a = a[:len(a)//3]

		elif x > triddle_b:
			a = a[len(a)//3 * 2:]

		elif x >= triddle_a and x <= triddle_b:
			a = a[len(a)//3:len(a)//3 * 2]

		if len(a) == 2:
			if a[0] == x or a[1] == x:
				return True
			else:
				return False

		triddle_a = a[len(a)//3]
		triddle_b = a[len(a)//3 * 2]

	return False
