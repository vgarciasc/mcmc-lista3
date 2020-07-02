import numpy as np
import matplotlib.pyplot as plt
import random as r
import math
import socket
import utils
import sys

def generate_uniform_letter():
	""" Samples uniformly from the alphabet """
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", \
		"i", "j", "k", "l", "m", "n", "o", "p", "q", "r", \
		"s", "t", "u", "v", "w", "x", "y", "z"]
	return letters[utils.uniform_discrete(0, len(letters) - 1)]

def generate_domain(j):
	""" Generates a domain with size 'j' """
	return "".join([generate_uniform_letter() for _ in range(j)])

def check_if_ufrj_domain_exists(domain):
	""" Checks if a certain subdomain exists within the UFRJ domain """
	full_url = "" + str(domain) + ".ufrj.br"

	try:
		socket.getaddrinfo(full_url, 80)
		return True
	except Exception as e:
		return False
	
def sample_L_size_domain(probs):
	""" Samples an integer in the interval [1..k], such that the probability of 'i' is 'probs[i]'. """
	sample = r.uniform(0, 1)

	for i, prob in enumerate(probs):
		sample -= prob
		if sample <= 0:
			return i + 1

	print("error")
	return -1

if __name__ == "__main__":
	param_1 = sys.argv[1] if len(sys.argv) > 1 else None
	param_2 = sys.argv[2] if len(sys.argv) > 2 else None

	if param_1 == '--help' or param_1 is None:
		print("USAGE: run this file in the following way:")
		print("  python q3.py [number of samples] [k]")
	elif utils.is_int(param_1):
		n = int(param_1)
		k = int(param_2)

		# |D_k|, that is, the amount of possible domains
		D_k_length = np.sum((26 ** i) for i in range(1, k + 1))
		# vector of probabilities of each size 'k'
		k_probs = [((26 ** i) / D_k_length) for i in range(1, k + 1)]

		# Generates 'n' domains
		domains = [generate_domain(sample_L_size_domain(k_probs)) for _ in range(n)]
		# Generates 'g(X)' based on generated domains
		g = [1 if check_if_ufrj_domain_exists(domain) else 0 for domain in domains]

		sample_mean = np.mean(g)
		Tk_est_final = sample_mean * D_k_length

		print("estimativa de domínios: " + str(Tk_est_final))
		print("domínios encontrados: " + str([domains[i] for i in range(0, len(g) - 1) if g[i] == 1]))

		plt.ylabel("estimativa do número de domínios")
		plt.xlabel("número de amostras")
		plt.plot(range(1, n), [np.mean(g[0:i]) * D_k_length for i in range(1, n)])
		plt.show()
	else:
		print("Incorrect parameters, run 'python q3.py --help' for USAGE.")
