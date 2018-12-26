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

# def funcarray(vars):
# 	x = vars[0]
# 	y = vars[1]
# 	z = vars[2]
# 	return [math.cos(x) + math.cos(y) + math.cos(z) -3/5, 
# 	math.cos(3*x) + math.cos(3*y) + math.cos(3*z), 
# 	math.cos(5*x) + math.cos(5*y) + math.cos(5*z)]

# def J(vars):
# 	x = vars[0]
# 	y = vars[1]
# 	z = vars[2]
# 	return [[-math.sin(x), -math.sin(y), -math.sin(z)],
# 	[-3*math.sin(3*x), -3*math.sin(3*y), -3*math.sin(3*z)],
# 	[-5*math.sin(5*x), -5*math.sin(5*y), -5*math.sin(5*z)]]



def func2(vars):
	newvars = np.zeros(len(vars))
	N = int(len(vars)/2)
	newvars[0] = vars[0] - xfixed - dt*vfixed
	newvars[1] = vars[1] - vfixed - dt*g
	for i in range(2, N, 2):
		x = vars[i]
		v = vars[i+1]
		newvars[i] = x - vars[i-2] - dt*vars[i-1]
		newvars[i+1] = v - vars[i-1] - dt*g
	return newvars


def J2(vars):
	N = int(len(vars)/2)
	J2 = np.zeros((2*N, 2*N))
	for i in range(2*N):
		J2[i][i] = 1
		try:
			J2[0][2*N-1] = 0
			J2[2*i][2*i-1] = -dt	
		except:
			try:
				J2[i+2][i] = -1
			except:
				continue
		try:
			J2[i+2][i] = -1
		except:
			continue
	print("J2", '\n', J2)
	return J2


def NRdimensions(funcarray, J, guessarray, count, tol):
	tolarray = tol*np.ones(len(guessarray))

	for i in range(0, count):
		print("this guess:", guessarray)
		Jinv = np.linalg.inv(J(guessarray))
		if np.linalg.det(Jinv) == 0:
			print(Jinv)
			print("Reached a local min/max in a function at", guessarray)
			break

		print("Jinv", '\n', Jinv, '\n')
		print("F", funcarray(guessarray), '\n')

		Y = np.dot(Jinv, funcarray(guessarray))

		print("Y", Y, '\n')
		print("guess", guessarray, '\n')
		if np.all(Y < tol) and np.all(Y > np.dot(-1, tol)):
			print("done at", guessarray, "count", i)
			print(funcarray(guessarray))
			return guessarray
		else:
			guessarray = np.subtract(guessarray, Y)

		print("guess is:", guessarray, '\n')
		# print("dx is:", J(guessarray))

	print("ran out of counts")

dt = 0.1

g = -9.8

xfixed = 1

vfixed = 1

guesses = [2, 2, 3, 3]

tol = 0.0001

NRdimensions(func2, J2, guesses, 50, tol)
