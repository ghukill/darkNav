import numpy
import random
import matplotlib.pyplot as plt


class Navigator(object):

	def __init__(self, name='ofNoName'):		
		self.coords = (0,0)
		self.alive = True
		self.name = name
		self.history = []
		self.history.append(self.coords)


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
		# print "movement_tuple",movement_tuple

		# update navigator location
		self.coords = tuple(numpy.add(self.coords, movement_tuple))

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

	def __init__(self):
		
		self.height = 10
		self.width = 10




if __name__ == "__main__":
	print "-----Entering darkNav-----"

	nav1 = Navigator('girgio')

	# random movements
	for _ in range(10000):
		nav1.randomMove(10)

	# prep to scatter
	from math import log
	plt.scatter(*zip(*nav1.history))
	plt.show()


