import curses

class Consolegame:

	def __init__(self):	
		self.logger = []
		
	def log(self, message):
		self.logger.append(message)
		
	def mainwrapper(self, window):
		self.window = window
		self.log(self.dimensions())
		self.main()
			
	def run(self):
		try:	
			curses.wrapper(self.mainwrapper)
		finally:
			for msg in self.logger:
				print msg

	def dimensions(self):
		self.width = self.window.getmaxyx()[1]
		self.height = self.window.getmaxyx()[0]

		return (self.height, self.width)
