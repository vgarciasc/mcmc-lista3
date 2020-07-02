import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import utils

def f(x):
	return 2 - x**2

def g(x, y):
	return 1 if y <= f(x) else 0

def generate_samples(N):
	""" Generates N samples of X, Y and g(X, Y) """
	
	samples_X_Y = np.array([(utils.uniform_continuous(0, 2), utils.uniform_continuous(0, 2)) for _ in range(N)])
	samples_g = np.array([g(pt[0], pt[1]) for pt in samples_X_Y])

	return samples_X_Y, samples_g

def estimate_sqrt_2(samples_g):
	""" Returns the estimate of sqrt(2) according to the provided samples """
	sample_mean = np.mean(samples_g)
	return 3 * sample_mean

def get_estimate_at_n(samples_g, n):
	""" Returns estimate of sqrt(2) according to the first 'n' samples """
	return estimate_sqrt_2(samples_g[0:n])

def display_illustration(samples_X_Y, samples_g):
	""" Plots the samples and colors them if inside or outside the curve (good for visualization) """
	points_under_curve = [pt for pt in samples_X_Y if g(pt[0], pt[1]) == 1]
	points_above_curve = [pt for pt in samples_X_Y if g(pt[0], pt[1]) == 0]

	plt.scatter([pt[0] for pt in points_above_curve], [pt[1] for pt in points_above_curve], color='red')
	plt.scatter([pt[0] for pt in points_under_curve], [pt[1] for pt in points_under_curve], color='blue')

	plt.plot(np.arange(0, math.sqrt(2), 0.1), [f(x) for x in np.arange(0, math.sqrt(2), 0.1)], color='black', linewidth=4, label='f(x)')
	plt.plot((0, 2), (0, 0), color='black')
	plt.plot((0, 0), (0, 2), color='black')
	plt.plot((2, 2), (0, 2), color='black')
	plt.plot((0, 2), (2, 2), color='black')
	plt.legend()
	plt.title("Amostragem com " + str(len(samples_X_Y)) + " pontos")
	plt.show()

def display_relative_error(N, samples_g):
	""" Plots the relative error of the estimates according to the samples """
	plt.yscale('log')
	plt.xscale('log')
	plt.plot(range(1, N), [utils.relative_error(get_estimate_at_n(samples_g, n), math.sqrt(2)) for n in range(1, N)])
	plt.ylabel('erro relativo do estimador')
	plt.xlabel('número de amostras consideradas')
	plt.show()

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None
	param_2 = sys.argv[2] if len(sys.argv) > 2 else None

	if param_1 == '--help' or param_1 is None:
		print("USAGE: run this file in the following way:")
		print("  python q1.py [number of samples] [flag]")
		print("Possible values for [flag]:")
		print("  EMPTY: default run.")
		print("  --display-illustration: displays illustration of sampled points on the interval.")
		print("  --display-error: display relative error graph.")
	elif utils.is_int(param_1):
		N = int(param_1)

		samples_X_Y, samples_g = generate_samples(N)
		
		final_estimate = estimate_sqrt_2(samples_g)
		final_relative_error = utils.relative_error(final_estimate, math.sqrt(2))

		print("sqrt(2) = " + str(final_estimate))
		print("relative error = " + str(final_relative_error))
		
		if param_2 == "--display-illustration":
			display_illustration(samples_X_Y, samples_g)
		elif param_2 == "--display-error":
			display_relative_error(N, samples_g)
	else:
		print("Incorrect parameters, run 'python q1.py --help' for USAGE.")
