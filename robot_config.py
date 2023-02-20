# import robot_model, math, and numpy
import robot_model
import math
import numpy as np

#test
def test(data):	
	'''
	passes through data in form of a 2d array. order of elements within is theta, a, d, alpha
	runs the data through the kinematic chain then gets and returns position (x,y,z) and rotation (roll,pitch,yaw)
	'''
	result = robot_model.kinematic_chain(data)
	return robot_model.get_pos(result), robot_model.get_rot(result)


def printResults(test):
	'''
	formats and prints results of transformations
	'''
	x = test[0][0]
	y = test[0][1]
	z = test[0][2]
	roll = test[1][0]
	pitch = test[1][1]
	yaw = test[1][2]
	print('x = {:.2f}'.format(x) + '\ny = {:.2f}'.format(y) + '\nz = {:.2f}'.format(z) + '\nroll = {:.2f}'.format(roll) + '\npitch = {:.2f}'.format(pitch) + '\nyaw = {:.2f}'.format(yaw))


if __name__ == '__main__':

	#2a:
	
	#testdata has theta = pi/2, a = 1, d = 0, alpha = 0 for both 1st and 2nd
	test1data = [[math.pi/2, 1, 0, 0],[math.pi/2, 1, 0, 0]]
	test1 = test(test1data)
	print('The first test:')
	printResults(test1)
	
	#2b:
	
	#uses DH params from slide 37
	#two cases:
	#case1:
	test2case1 = [[0, 0, 0.1625, math.pi/2],
			[0, -0.425, 0, 0],
			[0, -0.3922, 0, 0],
			[0, 0, 0.1333, math.pi/2],
			[0, 0, 0.0997, -math.pi/2],
			[0, 0, 0.0996, 0]]
	
	test2 = test(test2case1)
	print('The second test:')
	printResults(test2)
	
	#case2:
	test2case2 = [[0, 0, 0.1625, math.pi/2],
			[-math.pi/2, -0.425, 0, 0],
			[0, -0.3922, 0, 0],
			[0, 0, 0.1333, math.pi/2],
			[0, 0, 0.0997, -math.pi/2],
			[0, 0, 0.0996, 0]]
	
	test3 = test(test2case2)
	print('The third test:')
	printResults(test3)
