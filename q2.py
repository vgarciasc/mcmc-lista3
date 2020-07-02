import numpy as np
import matplotlib.pyplot as plt
import math
import utils
import sys

def generate_exponential_sample(L):
	""" Returns a sample from an exponential distribution """
	u = utils.uniform_continuous(0, 1)
	return - np.log(u) / L

def generate_pareto_sample(x_0, alpha):
	""" Returns a sample from a Pareto distribution """
	u = utils.uniform_continuous(0, 1)
	return x_0 / (u ** (1 / alpha))

def run_exponential(N, L, display=False):
	""" Runs the exponential distribution sampling (q2.1) """
	print("Generating " + str(N) + " samples from exponential distribution, with lambda = " + str(L) + ":")

	# Generates samples
	samples = [generate_exponential_sample(L) for _ in range(N)]

	# Calculates sample mean and sample variance
	sample_mean = np.mean(samples)
	sample_variance = np.var(samples, ddof=1)
	mean = 1 / L
	variance = 1 / (L ** 2)

	# Prints the estimates and their respective relative errors
	print("-- sample mean: " + str(sample_mean))
	print("-- mean relative error: " + str(utils.relative_error(sample_mean, mean)))
	print("-- variance: " + str(sample_variance))
	print("-- variance relative error: " + str(utils.relative_error(sample_variance, variance)))

	# Displays graph if necessary
	if display:
		plt.hist(samples, bins=100)
		plt.xlabel("x")
		plt.ylabel("amostras")
		plt.title(str(N) + " amostras de Distribuição Exponencial. Lambda = " + str(L))
		plt.show()

def run_pareto(N, x_0, alpha, display=False):
	""" Runs the Pareto distribution sampling (q2.2) """
	print("Generating " + str(N) + " samples from Pareto distribution with x_0 = " + str(x_0) + ", alpha: " + str(alpha))

	# Generates samples
	samples = [generate_pareto_sample(x_0, alpha) for _ in range(N)]

	# Calculates sample mean and sample variance
	sample_mean = np.mean(samples)
	sample_variance = np.var(samples, ddof=1)
	mean = (alpha * x_0) / (alpha - 1) if alpha > 1 else math.inf
	variance = ((x_0 ** 2) * alpha) / (((alpha - 1) ** 2) * (alpha - 2)) if alpha > 2 else math.inf

	# Prints the estimates and their respective relative errors
	print("-- sample mean: " + str(sample_mean))
	print("-- mean relative error: " + str(utils.relative_error(sample_mean, mean)))
	print("-- variance: " + str(sample_variance))
	print("-- variance relative error: " + str(utils.relative_error(sample_variance, variance)))

	# Displays graph if necessary
	if display:
		plt.hist(samples, bins=100)
		plt.xlabel("x")
		plt.ylabel("amostras")
		plt.title(str(N) + " amostras da Distribuição de Pareto. x_0 = " + str(x_0) + ", alpha = " + str(alpha))
		plt.show()

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None
	param_2 = sys.argv[2] if len(sys.argv) > 2 else None
	param_3 = sys.argv[3] if len(sys.argv) > 3 else None
	param_4 = sys.argv[4] if len(sys.argv) > 4 else None

	if param_1 == '--help' or param_1 is None:
		print("USAGE: run this file in the following way:")
		print("> Exponential Distribution (Q2.1):")
		print("    python q2.py --exponential [number of samples] [lambda]")
		print("> Pareto Distribution (Q2.2):")
		print("    python q2.py --pareto [number of samples] [x_0] [alpha]")
	elif param_1 == "--exponential":
		N = int(param_2)
		L = float(param_3)

		run_exponential(N, L, display=True)
	elif param_1 == "--pareto":
		N = int(param_2)
		x_0 = float(param_3)
		alpha = float(param_4)

		run_pareto(N, x_0, alpha, display=True)
	else:
		print("Incorrect parameters, run 'python q2.py --help' for USAGE.")