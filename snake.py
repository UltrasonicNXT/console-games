import curses, time, sys, random, os

width = 40
height = 20
sc = None
logger = ""

def paint(x, y, i):
	global sc
	sc.addstr(y, x*2, "  ", curses.color_pair(i))

def string(s, y):
	global sc
	sc.addstr(y, 39, s, curses.color_pair(3))
	
def feed():
	global height, width, sc
	
	x = random.choice(range(width))
	y = random.choice(range(height))
	f = random.choice(["OO", "BB", "MM", "XX", "ZZ", "WW", "QQ"])
	
	sc.addstr(y, x*2, f, curses.color_pair(1))
	return x, y, f
	
def refeed(x, y, f):
	sc.addstr(y, x*2, f, curses.color_pair(1))
	
def main(insc):	
	global sc, logger
	sc = insc
	wait = 0.18
	sc.nodelay(1)
	curses.start_color()
	curses.curs_set(0)

	solids = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]

	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW) 
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
	
	x, y = 1, 1
#	paint(12, 15, 2)
	#body = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1]]
	body = [[5, 5]]
	go = "d"
	score = 0
	heading = []

	while True:
		for lob in solids:
			paint(*lob, i=4)
		
		inp = sc.getch()
		print inp
		dir = ""
		if inp in range(256):
			dir = chr(inp)
		sc.clear()

                for lob in solids:
                        paint(*lob, i=4)
                                        			
		if heading == []:
			while True:
				heading = feed()
				if heading[:2] not in solids + body:
					break			
		refeed(*heading)
		
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
                		y = height - 1
                        else:
                        	y -= 1
                elif go == "d":
                	if x == width:
                		x = 0
                        else:
                        	x += 1
                elif go == "s":
                	if y == height:
                		y = 0
                        else:
                        	y += 1
                elif go == "a":
                	if x == 0:
                		x = width - 1
                        else:
                        	x -= 1                                       

		if (x, y) == heading[:2]:
			curses.beep()
			score += 1
			heading = []
		else:
			body.pop(0)
		
                body.append([x, y])		
#		string(str(x)+", "+str(y), 29)
#		string(str(body[:-1]), 22)
		if body[-1] in body[:-1] + solids:
			logger += "rage"
			logger += "\n"+str(body[-1])
			logger += "\n"+str(body)
			logger += "\n"+str(solids)
			for rage in range(5):
				curses.flash()
				time.sleep(0.25)
				curses.beep()
				time.sleep(0.25)
			break
		
		for point in body[:-1]:
			paint(*point, i=2)
		paint(*body[-1], i=5)		
		string(str(wait), 30)
		string("score: "+str(score), height+1)
		sc.move(height-1, 1)
		sc.refresh()
#		logger += str(wait)
		time.sleep(wait)

	
curses.wrapper(main)
print logger
