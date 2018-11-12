def NR(func, fprime, guess, count, tol):

	x = guess

	for i in range(0, count):

		fxn = func(x)
		fxnprime = fprime(x)
		dx = fxn/fxnprime

		print("guess is:", x)
		print("dx is:", dx)

		if dx < tol and dx > -tol:
			print("done at", x)
			return x
		else:
			x = x - dx
	
	print("ran out of counts")


def func(x):
	return x**3 - 1.

def fprime(x):
	return 3.*x**2



NR(func, fprime, 1.5, 20, 0.01)
