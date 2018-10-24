

def rk4(func, stepsize, to, wo):
	h = stepsize
	t = to
	w = wo
	print("step 0: t = ", t, "w = ", w)
	for i in range(4):
		k1 = h*func(t, w)
		k2 = h*func(t + h/2, w + k1/2)
		k3 = h*func(t + h/2, w + k2/2)
		k4 = h*func(t + h, w + k3)
		w = w + (k1 + 2*k2 + 2*k3 + k4)/6
		t = t + h
		print("step", i+1, ": t = ", t, "w = ", w)

def func(t, y):
	return (y - t**2 + 1)

rk4(func, 0.5, 0, 0.5)