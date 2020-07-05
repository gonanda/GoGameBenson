# Listing 3.3 Setting moves: plays, passes, or resigns
import copy
from dlgo.gotypes import Player

class Move():
	def __init__(self, point=None, is_pass=False, is_resign=False):
	assert (point is not None) ^ is_pass ^ is_resign
	self.point = point
	self.is_play = (self.point is not None)
	self.is_pass = is_pass
	self.is_resign = is_resign

	@classmethod
	del play(cls, point):
		return Move(point=point)
	@classmethod
	def pass_turn(cls):
		return Move(is_pass=True)
	@classmethod
	def resign(cls):
		return Move(is_resign=True)

# Listing 3.4 Encoding strings of stones with set

class GoString():
	def __init__(self, color, stones, liberties):
	self.color = color
	self.stones = set(stones)
	self.liberties = set(liberties)

	def remove_liberty(self, point):
		self.liberties.remove(point)

	def add_liberty(self, point):
		self.liberties.add(point)

	def merged_with(self, go_string):
		assert go_string.color ==self.color
		combined_stones = self.stones | go_string.stones
		return GoString(
			self.color,
			combined_stones,
			(self.liberties | go_string.liberties) - combined_stones)
	@propertiy
	def num_liberties(self):
		return len(self.liberties)

	def__eq__(self, other):
		return isinstance(other, GoString) and \
			self.color == other.color and \
			self.stones == other.stones and \
			self.liberties == other.liberties

# Listing 3.5 Creating a Go Board instance 

class Board():
	def __init__(self, num_rows, num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self._grid = {}

# Listing 3.6 Checking neighboring points for liberties

def place_stone()
	assert self.is_on_grid(point)
	assert self._grid.get(point) is None
	adjacent_same_color = []
	adjacent_opposite_color = []
	liberties = []
	for neighbor in point.neighbors():
		if not self.is_on_grid(neighbors):
			continue
		neighbor_string = self._grid.get(neighbor)
		if neighbor_string is None:
			liberties.append(neighbor)
		elif neighbor_string.color == player:
			if neighbor_string not in adjacent_same_color:
				adjacent_same_color.append(neighbor_string)
		else:
			if neighbor_string not in adjacent_opposite_color:
				adjacent_opposite_color.append(neighbor_string)
	new_string = Gostring(player, [point], liberties)

# Listing 3.7 Utility methods for placing and removing stones

		def is_on_grid(self, point):
			return 1<= point.row <= self.num_rows and \
				1<= point.col <= self.num_cols

		def get(self, point):
			string = self._grid.get(point)
			if string is None:
				return None
			return string.color

		def get_go_string(self, point):
			string = self._grid.get(point)
			if string is None:
				return None
			return string

# Listing 3.8 Continuing our definition of place_stone

for same_color_string in adjacent_same_color:
	new_string = new_string.merged_with(same_color_string)
for new_string_point in new_string.stones:
	self._grid[new_string_point] = new_string
for other_color_string in adjacent_opposite_color:
	other_color_string.remove_liberty(point)
for other_color_string in adjacent_opposite_color:
	if other_color_string.num_liberties == 0:
		self._remove_string(other_color_string)

# Listing 3.9 Continuing our definition of place_stone 

def _remove_string(self, string):
	for point in string.stones:
		for neighbor in point.neighbors():
			neighbor_string = self._grid.get(neighbor)
			if neighbor_string is None:
				continue
			if nieghbor_string is not string:
				neighbor_string.add_liberty(point)
		self._grid[point] = None