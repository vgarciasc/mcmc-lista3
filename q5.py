import random as r
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import pdb
import utils

# Uses h1(i) = 1 / N 
def run_h1(N, num_samples):
	h1 = lambda i : 1 / N

	h1_second_moment = N * sum([(g(i) ** 2) for i in range(1, N)])
	
	# Generating samples of Y1 = h1(i) for all 'i'
	Y1_samples = [utils.uniform_discrete(1, N) for _ in range(num_samples)]

	h1_samples = [g(i) / h1(i) for i in Y1_samples]
	h1_errors = [utils.relative_error(np.mean(h1_samples[0:i]), G_N) for i in range(1, num_samples, 100)]

	return h1_second_moment, h1_errors

# Uses h2(i) = i / K
def run_h2(N, num_samples):
	K = N * (N + 1) / 2
	h2 = lambda i : i / K

	h2_second_moment = K * sum([i * (np.log(i) ** 2) for i in range(1, N)])

	# Generating samples of Y2 = h2(i) for all 'i', using rejection sampling
	enveloper_density = lambda x : 1 / N
	enveloper_generate = lambda : utils.uniform_discrete(1, N)
	c = (N ** 2) / K
	Y2_samples = [utils.rejection_sampling(c, enveloper_density, enveloper_generate, h2) for _ in range(num_samples)]

	h2_samples = [g(i) / h2(i) for i in Y2_samples]
	h2_errors = [utils.relative_error(np.mean(h2_samples[0:i]), G_N) for i in range(1, num_samples, 100)]

	return h2_second_moment, h2_errors

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None
	param_2 = sys.argv[2] if len(sys.argv) > 2 else None

	if param_1 == '--help' or param_1 is None:
		print("USAGE: run this file in the following way:")
		print("  python q5.py [N] [number of samples]")

	elif utils.is_int(param_1):
		N = int(param_1)
		num_samples = int(param_2)

		g = lambda i : i * np.log(i)
		G_N = sum([g(i) for i in range(1, N)])

		h1_second_moment, h1_errors = run_h1(N, num_samples)
		h2_second_moment, h2_errors = run_h2(N, num_samples)

		# Outputting values		
		plt.plot(range(1, num_samples, 100), h1_errors, label='h1(i)')
		plt.plot(range(1, num_samples, 100), h2_errors, label='h2(i)')
		print("second moment of h1 : " + "{:.5e}".format(h1_second_moment))
		print("second moment of h2 : " + "{:.5e}".format(h2_second_moment))

		plt.xlabel('número de amostras')
		plt.ylabel('erro relativo')
		plt.xscale('log')
		plt.yscale('log')
		plt.legend()
		plt.show()

	else:
		print("Incorrect parameters, run 'python q1.py --help' for USAGE.")