import random

class Maze:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		#  nodes[(x, y)] ==> {North, South, East, West}
		self.nodes = {}
		self.generate()

	def generate(self):
		self.nodes = {}						#  Reset dictionary
		net = {}							#  Initialize temp dictionary
		for i in range(0, self.h):			#  For all rows...
			for j in range(0, self.w):		#  For all columns...
				self.nodes[(j, i)] = {}		#  Blank nodes
				net[(j, i)] = [random.randint(0, 100) for x in range(0, 4)]

		for i in range(0, self.h):
			for j in range(0, self.w):

				if net[(j, i)].index(min(net[(j, i)])) == 0 and (j, i - 1) in self.nodes.keys():
					self.nodes[(j, i)]['North'] = (j, i - 1)
					self.nodes[(j, i - 1)]['South'] = (j, i)

				elif net[(j, i)].index(min(net[(j, i)])) == 1 and (j, i + 1) in self.nodes.keys():
					self.nodes[(j, i)]['South'] = (j, i + 1)
					self.nodes[(j, i + 1)]['North'] = (j, i)

				elif net[(j, i)].index(min(net[(j, i)])) == 2 and (j + 1, i) in self.nodes.keys():
					self.nodes[(j, i)]['East'] = (j + 1, i)
					self.nodes[(j + 1, i)]['West'] = (j, i)

				elif (j - 1, i) in self.nodes.keys():
					self.nodes[(j, i)]['West'] = (j - 1, i)
					self.nodes[(j - 1, i)]['East'] = (j, i)
		return

	def draw(self):
		for y in range(0, self.h):
			outstr1 = ''
			outstr2 = ''
			outstr3 = ''
			for x in range(0, self.w):
				if 'North' not in self.nodes[(x, y)].keys():
					outstr1 += '---'
				else:
					outstr1 += '   '

				if 'South' not in self.nodes[(x, y)].keys():
					outstr3 += '---'
				else:
					outstr3 += '   '

				if 'West' not in self.nodes[(x, y)].keys():
					outstr2 += '| '
				else:
					outstr2 += '  '

				if 'East' not in self.nodes[(x, y)].keys():
					outstr2 += '|'
				else:
					outstr2 += ' '

			print(outstr1)
			print(outstr2)
			print(outstr3)
		return


class MazeBuilder:
	def __init__(self):
		return

	def build(self, w, h):
		m = Maze(w, h)
		m.generate()
		return m