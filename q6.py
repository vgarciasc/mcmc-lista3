import numpy as np
import matplotlib.pyplot as plt
import math
import utils
import sys

def generate_samples(alpha, a, b, num_samples):
	""" Generates samples from the f(X) distribution """
	f = lambda x : x ** alpha
	return [f(utils.uniform_continuous(a, b)) for _ in range(0, num_samples)]

def single_run(alpha, a, b, num_samples, step_size=100, display=False):
	""" Executes a single round of Monte Carlo method """

	# Calculates the true value of 'g(alpha, a, b)'
	g_real = (b ** (alpha + 1) - a ** (alpha + 1)) / (alpha + 1)

	# Generates samples f(X)
	samples = generate_samples(alpha, a, b, num_samples)

	# Calculate array of estimates and array of errors
	estimate_at_n = lambda samples, n : np.mean(samples[0:n]) * (b - a)
	estimates = [estimate_at_n(samples, i) for i in range(1, num_samples, step_size)]
	errors = [utils.relative_error(estimate, g_real) for estimate in estimates]

	# Display graph if necessary
	if display:
		label = "alpha: " + str(alpha) + ", a: " + str(a) + ", b: " + str(b)

		print(label)
		print("true value: " + str(g_real))
		print("final estimate: " + str(estimates[-1:]))
		print("final relative error: " + str(errors[-1:]))

		plt.yscale('log')
		plt.xscale('log')
		plt.plot(range(1, num_samples), errors, label = label)
		plt.ylabel('erro relativo')
		plt.xlabel('número de amostras')
		plt.legend()
		plt.show()

	return estimates, errors, g_real

def default_run(num_samples, step_size=100):
	""" Executes multiple rounds of Monte Carlo method (default run for question 6.4) """
	a = 0
	fig, axs = plt.subplots(3, 1)

	for i, b in enumerate([1, 2, 4]):
		ax = axs[i]

		for alpha in [1, 2, 3]:
			# Calculates a single round
			estimates, errors, g_real = single_run(alpha, a, b, num_samples, step_size=step_size)

			# Plots graph using relative error
			label = "alpha: " + str(alpha) + ", a: " + str(a) + ", b: " + str(b)
			ax.set_yscale('log')
			ax.set_xscale('log')
			ax.set_ylabel('erro relativo')
			ax.set_xlabel('número de amostras')
			ax.plot(range(1, num_samples, step_size), errors, label = label)
			ax.legend()
	
	plt.show()

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None
	param_2 = sys.argv[2] if len(sys.argv) > 2 else None
	param_3 = sys.argv[3] if len(sys.argv) > 3 else None
	param_4 = sys.argv[4] if len(sys.argv) > 4 else None

	num_samples = None
	alpha = None
	a = 0
	b = None

	if param_1 == "--help" or param_1 is None:
		print("USAGE: run this file in one of the following ways:")
		print("  1: python q6.py --default")
		print("  2: python q6.py [number of samples] [alpha] [a] [b]")

	elif param_1 == "--default":
		num_samples = 10 ** 6
		step_size = int(num_samples / 10 ** 4)

		default_run(num_samples)

	elif utils.is_int(param_1):
		num_samples = int(param_1)
		alpha = float(param_2)
		a = float(param_3)
		b = float(param_4)
		step_size = int(num_samples / 10 ** 4)

		single_run(alpha, a, b, num_samples, step_size=step_size, display=True)

	else:
		print("Incorrect parameters, run 'python q4.py --help' for USAGE.")


	