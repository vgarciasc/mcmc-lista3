import random as r
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def is_int(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

def uniform_continuous(start, end):
	return r.uniform(0, 1) * (end - start) + start

def uniform_discrete(start, end):
	return int(r.uniform(0, 1) * (end - start + 1)) + start

def relative_error(estimate, real):
	if real != 0:
		return abs(estimate - real) / real
	else:
		return relative_error(1 + estimate, 1)

def rejection_sampling(c, enveloper_density, enveloper_generate, h_density):
	while True:
		i = enveloper_generate()
		u = uniform_continuous(0, c * enveloper_density(i))
		if u <= h_density(i):
			return i