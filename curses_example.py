# import curses
#
# screen = curses.initscr()
# screen.refresh
# screen.getch()
# curses.endwin()

import curses
#init the curses screen
screen = curses.initscr()
screen.addstr(0,10,'Balconia Roast Logger v0.1')
#use cbreak to not require a return key press
curses.cbreak()
print "press q to quit"
quit=False
# loop
while quit !=True:
   c = screen.getch()
   print curses.keyname(c),
   if curses.keyname(c)=="q" :
      quit=True
