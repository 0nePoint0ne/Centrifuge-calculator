import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def displayData(size, speed):
	sizes = []
	force = []
	for i in range(size):
		sizes.append(int(i))
		force.append((speed*speed) * 1.118 * (10**-5) * i)
	ts = pd.Series(force,sizes)

	ts = ts.cumsum()
	
	for i in force:
		print(i)
	
	plt.title('G force vs Radius')
	plt.ylabel('G force (g)')
	plt.xlabel('Radius (cm)')
	
	ts.plot()
	plt.show()


def main():
	print("Object is 100 KG")
	size = int(input('Enter radius in cm: '))
	speed = int(input('RPM: '))
	#force = (speed*speed) * 1.118 * (10**-5) * size
	
	#print(force)
	if(size < 10000):
		displayData(size, speed)

main()