import curses, time, sys, random, os, cg

class Snake(cg.Consolegame):

	def paint(self, x, y, i):
		self.window.addstr(y, x*2, "  ", curses.color_pair(i))
	
	def string(self, s, y):
		xpos = (self.width/2)-len(s)
		self.window.addstr(y, xpos, s, curses.color_pair(3))
		
	def feed(self):
		x = random.choice(range(self.gamewidth))
		y = random.choice(range(self.gameheight))
		f = random.choice(["OO", "BB", "MM", "XX", "ZZ", "WW", "QQ"])
		
		self.window.addstr(y, x*2, f, curses.color_pair(1))
		return x, y, f
	
	def refeed(self, x, y, f):
		self.window.addstr(y, x*2, f, curses.color_pair(1))
	
	def main(self):
		self.gamewidth = (self.width/2)-1
		self.gameheight = (self.height-2)-1
		
		wait = 0.18
		self.window.nodelay(1)
		curses.start_color()
		curses.curs_set(0)

		solids = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]

		curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
		curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW) 
		curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
		curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
		
		x, y = 1, 1
		body = [[5, 5]]
		go = "d"
		score = 0
		heading = []

		while True:
			for lob in solids:
				self.paint(*lob, i=4)
		
			inp = self.window.getch()
			print inp
			dir = ""
			if inp in range(256):
				dir = chr(inp)
			self.window.clear()

	                for lob in solids:
	                        self.paint(*lob, i=4)
                                        			
			if heading == []:
				while True:
					heading = self.feed()
					if heading[:2] not in solids + body:
						break			
			self.refeed(*heading)
			
			if dir == "w":
				go = "w"
			elif dir == "d":
				go = "d"
			elif dir == "s":
				go = "s"
			elif dir == "a":
				go = "a"
			elif dir == "r":
				wait += 0.05
			elif dir == "f":
				wait -= 0.05
			elif dir == "q":
				break

	                if go == "w":
	                	if y == 0:
	                		y = self.gameheight - 1
	                        else:
	                        	y -= 1
	                elif go == "d":
	                	if x == self.gamewidth:
	                		x = 0
	                        else:
	                        	x += 1
	                elif go == "s":
	                	if y == self.gameheight:
	                		y = 0
	                        else:
	                        	y += 1
	                elif go == "a":
	                	if x == 0:
	                		x = self.gamewidth - 1
	                        else:
	                        	x -= 1                                       

			if (x, y) == heading[:2]:
				curses.beep()
				score += 1
				heading = []
			else:
				body.pop(0)
		
	                body.append([x, y])
			if body[-1] in body[:-1] + solids:
				for rage in range(5):
					curses.flash()
					time.sleep(0.25)
					curses.beep()
					time.sleep(0.25)
				break
		
			for point in body[:-1]:
				self.paint(*point, i=2)
			self.paint(*body[-1], i=5)		
			self.string("speed: "+str(wait), self.height-2)
			self.string("score: "+str(score), self.height-1)
			self.window.move(self.height-1, 1)
			self.window.refresh()
			time.sleep(wait)

snake = Snake()
snake.run()
