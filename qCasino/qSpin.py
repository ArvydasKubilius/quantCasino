import qHelpers 

MAX = 36
POWER = 6

def spin():
	n = qHelpers.random_int(POWER)
	while n > MAX:
		n = qHelpers.random_int(POWER)
	return n