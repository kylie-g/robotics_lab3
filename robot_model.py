# import math and numpy
import math
import numpy as np

#dh_transformation
def dh_transformation(theta, a, d, alpha):
	'''
	recieves the denavit-hartenberg params
	returns a combined homogenous tranformation
	'''
	result = [[math.cos(theta), -math.sin(theta)*math.cos(alpha), math.sin(theta)*math.sin(alpha), a*math.cos(theta)],
		[math.sin(theta), math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha), a*math.sin(theta)],
		[0, math.sin(alpha), math.cos(alpha), d],
		[0, 0, 0, 1]]
	return result


#kinematic chain
def kinematic_chain(DHArray):
	'''
	recieves a 2d list/array containing the DH params
	array order: theta, a, d, alpha
	returns a homogenous transformation for the kinetic chain (combo of the transformations for all the frames)
	'''
	#initialized total transformation array
	totalArray = np.identity(4)
	#loop that scans the rows and multiplies the transformation
	for row in DHArray:
		totalArray = np.matmul(totalArray, dh_transformation(row[0], row[1], row[2], row[3]))
	return totalArray


#get_pos
def get_pos(htrans):
	'''
	recieves homogeneous transformation as input (an array)
	returns the x, y, z components of the position
	'''
	#h14 is x -> [0][3]
	#h24 is y -> [1][3]
	#h34 is z -> [2][3]
	return htrans[0][3], htrans[1][3], htrans[2][3]
	

#get_rot
def get_rot(htrans):
	'''
	recieves a homogeneous transformation as input (array)
	roll-pitch-yaw = fixed frame
	returns calculated roll-pitch-yaw
	
	roll = arctan(h32/h33)
	pitch = arctan(-h31/(sqrt(h32^2+h33^2)))
	yaw = arctan(h21/h11)
	
	array = [[h11, h12, h13]
			[h21, h22, h23]
			[h31, h32, h33]]
	'''
	
	h32 = htrans[2][1]
	h33 = htrans[2][2]
	h31 = htrans[2][0]
	h21 = htrans[1][0]
	h11 = htrans[0][0]
	
	#use atan2 to get range -pi to pi (atan range gives -pi/2 to pi/2)
	
	#calculate roll, pitch, yaw based on formulas
	roll = math.atan2(h32, h33)
	pitch = math.atan2(-h31, math.sqrt(h32**2+h33**2))
	yaw = math.atan2(h21, h11)
	
	return roll, pitch, yaw
	
