import curses
from curses import wrapper
import time
import random


def get_text():
	with open("text.txt" ,'r')as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def start_screen(stdscr):
	# Clearing screen before printing anything
	stdscr.clear()

	# Printing str on clear screen and adding color_pair id 1 and position on terminal
	stdscr.addstr("Welcome to the Typing Speed Check!\nPress any key to begin")

	# Refreshing the original screen
	stdscr.refresh()
	stdscr.getkey()	


def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}", curses.color_pair(4))
	for i, char in enumerate(current):
		correct_char = target[i]

		if char == correct_char:
			stdscr.addstr(0, i, char, curses.color_pair(1))
		else:
			stdscr.addstr(0, i, char, curses.color_pair(2))

def speed_test(stdscr):
	target_text = get_text()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)


		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)

		stdscr.refresh()
		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		
		try:
			key = stdscr.getkey()
		except:
			continue

		# Breaking when the escape key is pressed
		if ord(key) == 27:
			break

		if key in ["KEY_BACKSPACE", '\b', '\x7f']:
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
				current_text.append(key)
		else:
			break


def main(stdscr):
	# Changing text and background colors
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)# Correct
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)# Wrong
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)# Default
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)# Default

	# Initializing the screen
	start_screen(stdscr)

	while True:
		speed_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()

		if ord(key) == 27:
			break

	# Making the screen stay with the str untill any key is pressed
	try:
		key = stdscr.getkey()
	except:
		pass

# Initializing curses
wrapper(main)


"""
curses.init_pair(id, foreground color, background color)
stdscr.addstr(line, column, string, color)

"""