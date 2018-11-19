import numpy as np
import math
# import symengine as sym


# def Jacobian(funcarray, vararray):
# 	J = np.empty(shape(len(funcarray), len(vararray)))
# 	for i in range(len(funcarray)):
# 		func = funcarray[i]
# 		for j in range(len(vararray)):
# 			var = vararray[j]
# 			J[i][j] = sym.diff(func, var)
# 	return J

def funcarray(vars):
	x = vars[0]
	y = vars[1]
	z = vars[2]
	# return [vars[0]**2 - 5, vars[1]**2, (vars[2]**2)/2]
	return [math.cos(x) + math.cos(y) + math.cos(z) -3/5, math.cos(3*x) + math.cos(3*y) + math.cos(3*z), math.cos(5*x) + math.cos(5*y) + math.cos(5*z)]

def J(vars):
	x = vars[0]
	y = vars[1]
	z = vars[2]
	return [[-math.sin(x), -math.sin(y), -math.sin(z)],
	[-3*math.sin(3*x), -3*math.sin(3*y), -3*math.sin(3*z)],
	[-5*math.sin(5*x), -5*math.sin(5*y), -5*math.sin(5*z)]]
	# return [[2*vars[0], 0, 0],
	# [0, 2*vars[1], 0],
	# [0, 0, vars[2]]]



def NRdimensions(funcarray, J, guessarray, count, tol, ntol):

	for i in range(0, count):
		Jinv = np.linalg.inv(J(guessarray))
		print("Jinv", Jinv, '\n')
		print("F", funcarray(guessarray), '\n')
		Y = np.dot(Jinv, funcarray(guessarray))
		print("Y", Y, '\n')
		print("guess", guessarray, '\n')

		if np.all(Y < tol) and np.all(Y > ntol):
			print("done at", guessarray)
			return guessarray
		else:
			guessarray = np.subtract(guessarray, Y)

		# print("guess is:", guessarray)
		# print("dx is:", J(guessarray))

	print("ran out of counts")



guesses = [3, 1, 2]

tol = [0.001, 0.0001, 0.0001]

ntol = [-0.0001, -0.0001, -0.0001]

NRdimensions(funcarray, J, guesses, 200, tol, ntol)


