import curses
from curses import wrapper
import time
import random 


class snake_render():

    snake_list = []
    vector = None
    head = [[]]
    i=0
    game_over = 3
  
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        snake_render.snake_list = [[0,0]]*size
        for i in range(size):
            snake_render.snake_list[i] = [x+i,y]
        snake_render.head[0] = snake_render.snake_list[0]


    def render_screen(self, stdscr):
        
        self.stdscr = stdscr
            
        if snake_render.head[0][0] < 1 or snake_render.head[0][0] >= curses.COLS-2 or snake_render.head[0][1] < 1 or snake_render.head[0][1] >= curses.LINES-2 or snake_render.head[0] in snake_render.snake_list[1:]:
            snake_render.game_over -= 1
            snake_render.head = [[curses.COLS//2,curses.LINES//2]]
        else:
            self.stdscr.addstr(snake_render.head[0][1],snake_render.head[0][0],"x")
            for c in range(len(snake_render.snake_list)-1, 0, -1):
                self.stdscr.addstr(snake_render.snake_list[c][1],snake_render.snake_list[c][0],"o")

    def render_screen_over(self, stdscr, row, col):
        self.stdscr = stdscr
        self.row = row
        self.col = col
        self.stdscr.addstr(1,1,"Points: {} | Lives: {} | Exit press Q | Control by arrow keys".format(snake_eats.eats, snake_render.game_over))
        for x in range(curses.COLS-2):
            self.stdscr.addstr(0,x,'*')
            self.stdscr.addstr(curses.LINES-2, x, '*')
        for y in range(curses.LINES-2):
            self.stdscr.addstr(y,0,'*')
            self.stdscr.addstr(y, curses.COLS-2, '*')           
      
    def move_head(self, key, stdscr):
        self.key = key
        self.stdscr = stdscr
       
        
        if self.key == curses.KEY_UP or snake_render.vector == 'top':
            snake_render.vector = 'top'
            snake_render.head[0][1] -= 1
        if self.key == curses.KEY_DOWN or snake_render.vector == 'down':
            snake_render.vector = 'down'
            snake_render.head[0][1]  += 1
        if self.key == curses.KEY_RIGHT or snake_render.vector == 'right':
            snake_render.vector = 'right'
            snake_render.head[0][0] += 1
        if self.key == curses.KEY_LEFT or snake_render.vector == 'left':
            snake_render.vector = 'left'
            snake_render.head[0][0] -= 1
        if key == ord('q'):
            snake_render.game_over = 0
          
        if snake_render.vector: 
           for d in range(len(snake_render.snake_list)-1, 0, -1):
              if snake_render.vector:
                  snake_render.snake_list[d] = snake_render.snake_list[d-1]        
        snake_render.snake_list[0] = snake_render.head[0].copy()    



class  snake_eats():
    eats = 0
    eats_xy = [3,2]

    def __init__(self):
        pass

    def add_point(self, stdscr):
        self.stdscr = stdscr 
        self.stdscr.addstr(snake_eats.eats_xy[1],snake_eats.eats_xy[0],'@')
        if snake_render.head[0] == snake_eats.eats_xy:
            snake_render.snake_list.append([0,0])
            snake_eats.eats += 1
            self.eats_add()

    def eats_add(self):
        snake_eats.eats_xy = [random.randint(1,curses.COLS-3),random.randint(1,curses.LINES-3)]

def main(stdscr):
    
    snakeob = snake_render(3,5,5)
    eatsob = snake_eats()
    eatsob.eats_add()

    stdscr.nodelay(True)

    while snakeob.game_over:

        key = stdscr.getch()
        
        
        snakeob.move_head(key, stdscr)


        stdscr.clear()

        snakeob.render_screen_over(stdscr, 1, 2)
        snakeob.render_screen(stdscr)
        eatsob.add_point(stdscr)

        stdscr.refresh()
        time.sleep(.20)

wrapper(main)