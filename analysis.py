import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib
import math

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def analyze():
	c5 = open('chaos5.txt').readlines()
	c7 = open('chaos7.csv').readlines()

	t_5, x_inner_5, y_inner_5, v_inner_5, theta_inner_5, omega_inner_5, x_outer_5, y_outer_5, v_outer_5, theta_outer_5, omega_outer_5 = [],[],[],[],[],[],[],[],[],[],[]
	t_7, x_inner_7, y_inner_7, v_inner_7, theta_inner_7, omega_inner_7, x_outer_7, y_outer_7, v_outer_7, theta_outer_7, omega_outer_7 = [],[],[],[],[],[],[],[],[],[],[]

	ti = 0
	for line in c5:
		if 't' in line: continue
		terms = line.split('\t')
		if len(t_5) == 0:
			ti = float(terms[0])
		t_5.append(float(terms[0]) - ti); 
		x_inner_5.append(float(terms[1])); y_inner_5.append(float(terms[2])); v_inner_5.append(float(terms[3])); theta_inner_5.append(float(terms[4])); omega_inner_5.append(float(terms[5]))
		x_outer_5.append(float(terms[6])); y_outer_5.append(float(terms[7])); v_outer_5.append(float(terms[8])); theta_outer_5.append(float(terms[9])); omega_outer_5.append(float(terms[10]))

	for line in c7:
		if 't' in line: continue
		terms = line.split(',')
		if len(t_7) == 0:
			ti = float(terms[0])
		t_7.append(float(terms[0]) - ti); 
		x_inner_7.append(float(terms[1])); y_inner_7.append(float(terms[2])); v_inner_7.append(float(terms[3])); theta_inner_7.append(float(terms[4])); omega_inner_7.append(float(terms[5]))
		x_outer_7.append(float(terms[6])); y_outer_7.append(float(terms[7])); v_outer_7.append(float(terms[8])); theta_outer_7.append(float(terms[9])); omega_outer_7.append(float(terms[10]))

	cum_theta_inner_5, cum_theta_outer_5 = [], []
	cum_theta_inner_7, cum_theta_outer_7 = [], []

	for n,angle in enumerate(theta_outer_5):
		if n == 0: cum_theta_outer_5.append(angle); continue

		angle_diff = theta_outer_5[n] - theta_outer_5[n-1]
		if theta_outer_5[n] > 5.5 and theta_outer_5[n-1] < 0.5:
			angle_diff -= 2*math.pi
		elif theta_outer_5[n] < 0.5 and theta_outer_5[n-1] > 5.5:
			angle_diff += 2*math.pi

		cum_theta_outer_5.append(angle_diff + cum_theta_outer_5[n-1])

	for n,angle in enumerate(theta_outer_7):
		if n == 0: cum_theta_outer_7.append(angle); continue

		angle_diff = theta_outer_7[n] - theta_outer_7[n-1]
		if theta_outer_7[n] > 5.5 and theta_outer_7[n-1] < 0.5:
			angle_diff -= 2*math.pi
		elif theta_outer_7[n] < 0.5 and theta_outer_7[n-1] > 5.5:
			angle_diff += 2*math.pi

		cum_theta_outer_7.append(angle_diff + cum_theta_outer_7[n-1])

	t_div, divergence = [], []

	for n,angle in enumerate(cum_theta_outer_5):
		t_div.append(t_5[n])
		divergence.append(abs(cum_theta_outer_5[n] - cum_theta_outer_7[n]))
		if t_5[n] >= 3.0: break

	#plt.plot(t_5, cum_theta_outer_5, 'b-', t_7, cum_theta_outer_7, 'r-')

	f = open('divergence.txt','w+')

	for n,val in enumerate(t_div):
		f.write(str(t_div[n])+','+str(divergence[n])+'\n')

	f.close()

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(t_div,divergence)
	plot.set_xlabel('time (s)', fontsize=20)
	plot.set_ylabel('angle difference', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(t_5, cum_theta_outer_5, 'b-', label='Chaos5') 
	plot.plot(t_7, cum_theta_outer_7, 'r-', label='Chaos7')
	plot.set_xlabel('time (s)', fontsize=20)
	plot.set_ylabel('Cumulative Angle', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)
	plot.legend()

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(x_inner_5, y_inner_5, 'b-', label='Chaos5') 
	plot.plot(x_inner_7, y_inner_7, 'r-', label='Chaos7')
	plot.set_xlabel('inner x', fontsize=20)
	plot.set_ylabel('inner y', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)
	plot.legend()

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(x_outer_5, y_outer_5, 'b-', label='Chaos5') 
	plot.plot(x_outer_7, y_outer_7, 'r-', label='Chaos7')
	plot.set_xlabel('outer x', fontsize=20)
	plot.set_ylabel('outer y', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)
	plot.legend()

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(theta_inner_5, omega_inner_5, 'b,', label='Chaos5') 
	plot.plot(theta_inner_7, omega_inner_7, 'r,', label='Chaos7')
	plot.set_xlabel('inner theta', fontsize=20)
	plot.set_ylabel('inner omega', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)
	plot.legend()

	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.plot(theta_outer_5, omega_outer_5, 'b,', label='Chaos5') 
	plot.plot(theta_outer_7, omega_outer_7, 'r,', label='Chaos7')
	plot.set_xlabel('outer theta', fontsize=20)
	plot.set_ylabel('outer omega', fontsize=20)
	plot.tick_params(axis='both', which='major', labelsize=20)
	plot.tick_params(axis='both', which='minor', labelsize=20)
	plot.legend()

	plt.show()

analyze()
