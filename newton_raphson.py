def NR(input_function, input_fprime, input_guess, count, tolerance):

	x = input_guess

	for i in range(0, count):

		fxn = input_function(x)
		fxnprime = input_fprime(x)
		if fxnprime == 0:
			print("reached a local max/min at", x)
			break
		try:
			dx = fxn/fxnprime
		except Exception as e:
			print(e)
			print("Try a different guess input!")
			break

		print("guess is:", x)
		print("dx is:", dx, '\n')

		if dx < tolerance and dx > -tolerance:
			print("done at", x)
			return x
		else:
			x = x - dx
	
	print("ran out of counts; try a different inital guess!")


def func(x):
	return x**2-2.

def fprime(x):
	return 2.*x

guess = 1

count = 100

tol = 0.001

NR(func, fprime, guess, count, tol)
