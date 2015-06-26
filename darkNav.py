import numpy
import requests


class Navigator(object):

	def __init__(self):		
		self.coords = (0,0)
		self.alive = True


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
		print "movement_tuple",movement_tuple

		# update navigator location
		self.coords = tuple(numpy.add(self.coords, movement_tuple))
		print "New location:",self.coords


class Arena(object):

	def __init__(self):
		pass
		
