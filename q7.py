import random as r
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import utils
import pdb

def sample_subset(a, k):
	""" Creates a subset of array 'a' with only 'k' elements """
	n = len(a)

	for i in range(0, k):
		u = utils.uniform_discrete(0, n - 1 - i)

		aux = a[u]
		a[u] = a[n - 1 - i]
		a[n - 1 - i] = aux

	return a[n-k:n]

def single_run(arr, n, k):
	""" Executes a single round of the 'sample_subset' method, returning the elapsed time """
	start_time = time.time()
	sample = sample_subset(arr, k)
	end_time = time.time()

	time_elapsed = end_time - start_time
	return time_elapsed

if __name__ == '__main__':
	Ns = [10 ** 4, 10 ** 6, 10 ** 8]
	Ks = [10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4]
	r = 10 ** 3

	for i in range(0, len(Ns)):
		n = Ns[i]
		arr = [1 for i in range(n)]

		data_points = []
		for j in range(0, len(Ks)):
			k = Ks[j]

			# Executes multiple rounds of the method, for calculating the mean time
			mean_time = np.mean([single_run(arr, n, k) for _ in range(r)])
			data_points.append(mean_time)
		
		# Plots the mean time
		plt.plot(Ks, data_points, label=('n: ' + str(n)))

	plt.xlabel("tamanho 'k' do subconjunto")
	plt.ylabel("tempo médio de execução (seg)")
	plt.xscale('log')
	plt.legend()
	plt.show()
