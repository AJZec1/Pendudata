import matplotlib.pyplot as plt
import math

def analyze():
	c5 = open('chaos5.txt').readlines()
	c6 = open('chaos6.txt').readlines()

	t, x_inner, y_inner, v_inner, theta_inner, omega_inner, x_outer, y_outer, v_outer, theta_outer, omega_outer = [],[],[],[],[],[],[],[],[],[],[]

	for line in c5:
		if 't' in line: continue
		terms = line.split('\t')
		t.append(float(terms[0])); 
		x_inner.append(float(terms[1])); y_inner.append(float(terms[2])); v_inner.append(float(terms[3])); theta_inner.append(float(terms[4])); omega_inner.append(float(terms[5]))
		x_outer.append(float(terms[6])); y_outer.append(float(terms[8])); v_outer.append(float(terms[7])); theta_outer.append(float(terms[9])); omega_outer.append(float(terms[10]))

	cum_theta_inner, cum_theta_outer = [], []

	for n,angle in enumerate(theta_outer):
		if n == 0: cum_theta_outer.append(angle); continue

		angle_diff = theta_outer[n] - theta_outer[n-1]
		if theta_outer[n] > 5.5 and theta_outer[n-1] < 0.5:
			angle_diff -= 2*math.pi
		elif theta_outer[n] < 0.5 and theta_outer[n-1] > 5.5:
			angle_diff += 2*math.pi

		cum_theta_outer.append(angle_diff + cum_theta_outer[n-1])

	plt.plot(t, cum_theta_outer)
	plt.show()

analyze()
