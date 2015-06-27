import numpy
import random
import matplotlib.pyplot as plt
import argparse


class Navigator(object):

	def __init__(self, name='Unknown', arena=(5000,5000)):				
		self.coords = (0,0)
		self.alive = True
		self.name = name
		self.history = []
		self.history.append(self.coords)
		self.arena = Arena(width=arena[0], height=arena[1])


	def move(self, direction, distance):

		def invalidInputs(msg):
			print msg
			return False

		# statics
		directions = ['n','e','s','w']

		# check inputs 
		try:
			# check direction
			direction = direction.lower()
			if direction not in directions:
				return invalidInputs("Could not parse direction.  Should be cardinal direction (e.g. n,e,s,w)")

			# check distance
			if not isinstance(distance, (int, long, float, complex)):
				return invalidInputs("Could not parse distance.  Should be integer (e.g. 1,10,100)")
		
		except Exception,e:
			return invalidInputs(e)


		# translate cardinal into quadrant integer tuple
		dir_trans = {
			"n" : (0,1),
			"e" : (1,0),
			"s" : (0,-1),
			"w" : (-1,0)
		}

		# create tuple
		movement_tuple = tuple(numpy.multiply(dir_trans[direction],distance))

		# try to move within arena
		attempt_coords = numpy.add(self.coords, movement_tuple)

		# check x
		if attempt_coords[0] > self.arena.width:
			attempt_coords[0] = self.arena.width
		if attempt_coords[0] < -(self.arena.width):
			attempt_coords[0] = -(self.arena.width)

		# check y
		if attempt_coords[1] > self.arena.height:
			attempt_coords[1] = self.arena.height
		if attempt_coords[1] < -(self.arena.height):
			attempt_coords[1] = -(self.arena.height)

		self.coords = tuple(attempt_coords)

		# update history
		self.history.append(self.coords)

	# random move
	def randomMove(self,max_distance):

		# random direction
		dir_dict = {
			1:'n',
			2:'e',
			3:'s',
			4:'w'
		}
		direction = dir_dict[int(random.random() * 4) + 1]

		# random distance
		flip = {
			False:-1,
			True:1
		}
		distance = (flip[bool(random.getrandbits(1))]) * (int(random.random() * max_distance) + 1)

		# debug
		self.move(direction,distance)



class Arena(object):

	def __init__(self,height,width):
		self.height = height
		self.width = width




if __name__ == "__main__":
	print "-----Entering darkNav-----"
	print "reticulating splines..."

	# parse arguments
	parser = argparse.ArgumentParser(description='Variables for darkNav')

	parser.add_argument("--numNavs", type=int, help="Number of navigators to generate",default=4)
	parser.add_argument("--arenah", type=int, help="Arena Height (radiating from 0,0)",default=500)
	parser.add_argument("--arenaw", type=int, help="Arena Width (radiating from 0,0)",default=500)
	parser.add_argument("--iterations", type=int, help="Number of times to move",default=5000)
	parser.add_argument("--maxMove", type=int, help="Maximum distance navigator can move randomly",default=10)

	args = parser.parse_args()

	# create navigators
	navigators = [Navigator(arena=(args.arenaw,args.arenah)) for i in range(args.numNavs)]

	# random movements
	for _ in range(args.iterations):
		for nav in navigators:
			nav.randomMove(args.maxMove)
	

	# prep to scatter
	print "graphing results..."
	from math import log
	for nav in navigators:
		plt.plot(*zip(*nav.history))
	plt.show()


