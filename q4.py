import numpy as np
import matplotlib.pyplot as plt
import math
import utils
import sys

def generate_envelope_sample(L):
	""" Samples from enveloping distribution """
	u = utils.uniform_continuous(0, 1)
	if u < 0.5:
		return np.log(2 * u) / L
	else:
		return - np.log(2 * (1 - u)) / L

def generate_normal_sample_by_rejection():
	""" Samples from normal distribution by using rejection sampling """
	L = 2 / math.sqrt(2 * math.pi)
	c = math.exp(1 / math.pi)

	# Defines density functions
	envelope_density = lambda x : 0.5 * L * math.exp(- L * x) if x > 0 else 0.5 * L * math.exp(L * x)
	normal_density = lambda x : (1 / math.sqrt(2 * math.pi)) * math.exp(- (x**2) * (1/2))

	# Rejection sampling algorithm
	while True:
		i = generate_envelope_sample(L)
		u = utils.uniform_continuous(0, c * envelope_density(i))
		if u <= normal_density(i):
			return i

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None

	if param_1 == "--help" or param_1 is None:
		print("USAGE: run this file in the following way:")
		print("  python q4.py [number of samples]")
	elif utils.is_int(param_1):
		N = int(param_1)

		print("Generating Z ~ Normal(mean = 0, variance = 1):")

		samples = [generate_normal_sample_by_rejection() for _ in range(N)]
		sample_mean = np.mean(samples)
		sample_variance = np.var(samples, ddof=1)

		print("-- sample mean: " + str(sample_mean))
		print("-- mean relative error: " + str(utils.relative_error(sample_mean, 0)))
		print("-- variance: " + str(sample_variance))
		print("-- variance relative error: " + str(utils.relative_error(sample_variance, 1)))

		plt.hist(samples, 100)
		plt.title("total de " + str(N) + " amostras")
		plt.ylabel("amostras")
		plt.xlabel("x")
		plt.show()
	else:
		print("Incorrect parameters, run 'python q4.py --help' for USAGE.")