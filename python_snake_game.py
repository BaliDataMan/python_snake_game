#pythonSnake Tutorial Python

# Consider number Line -->  for direction of X, Y(dirX,dirY) or value of X,Y(pos[0], pos[1])
# "surface" variable is windows of size width*width
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class block(object):
    rows = 20
    w = 500
    def __init__(self,start,dirX=1,dirY=0,color=( 87, 233, 10)): #this is pythonSnake's colour and dirX =1 coz we want our snake to move in right direction intially..
        self.pos = start
        self.dirX = 1
        self.dirY = 0
        self.color = color


    def move(self, dirX, dirY):
        self.dirX = dirX
        self.dirY = dirY
        self.pos = (self.pos[0] + self.dirX, self.pos[1] + self.dirY) # pos[0] + dirX means value of X and direction of X
                                                                    # pos[1] + dirY means value of Y and direction of Y and that would be the final position of snake in variable "pos"
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2)) # i*dis+1 and j*dis+1 is to draw snake boy_dir with  snake head only..
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)




class pythonSnake(object):
    boy_dir = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = block(pos)
        self.boy_dir.append(self.head)
        self.dirX = 0 # just keeping trcak of direction
        self.dirY = 1 # just keeping trcak of direction

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #if clicked on cross, window closed
                pygame.quit()

            keys = pygame.key.get_pressed()  #input from keyboard

            for key in keys:   # values of dirX and dirY is based on number line of X and y..
                if keys[pygame.K_LEFT]:
                    self.dirX = -1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY] # "turns" is dictionary, here assining turn[KEY] = [VALUE_X,VALUE_Y] , these values will decide the direction of snake's head..

                elif keys[pygame.K_RIGHT]:
                    self.dirX = 1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_UP]:
                    self.dirX = 0
                    self.dirY = -1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_DOWN]:
                    self.dirX = 0
                    self.dirY = 1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        #Now we will check the value( value_X and Value_Y ) of key(position) of dictionary "turns" to move accordingly LEFT,RIGHT,UP or DOWN..
        for i, c in enumerate(self.boy_dir):   # enumerating one by one from head to  tail(boy_dir of snake)
            p = c.pos[:]   # copying posistion of snakes's head, which we have assinged in above loop..
            if p in self.turns:   #if head's position(key) lies in turns(dictionary)
                turn = self.turns[p]  # assining VALUE of dictionary "turns" at position "p" to variable "turn"
                c.move(turn[0],turn[1])  #move head in direction of turn[0](vale_X) and y=turn[1](Value_y)
                if i == len(self.boy_dir)-1: # at the tail block
                    self.turns.pop(p) # we're removing the position(keys), so that after turn of snake's tail, we can assing new values in future, else it will repeat this turn and then which you will provide it..
            else: # if non of the above cases..  # Also Consider number Line of mathematics-->  for direction of X, Y(dirX,dirY) or value of X,Y(pos[0], pos[1])
                if c.dirX == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])    # LEFT TURN --> if dir == left and x == 0(first row), then assing x=19(last row) and y = same as previous
                elif c.dirX == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])    # RIGHT TURN --> if dir == right and x == 19, then assing x=0 and y = same as previous
                elif c.dirY == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)   # DOWN TURN --> if dir == down and y == 19, then assing x= same as previous and y = 0
                elif c.dirY == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)   # UP TURN --> if dir == up and y == 0, then assing x= same as previous and y = 19
                else: c.move(c.dirX,c.dirY) #if nothing pressed, nor x == 0 or 19 and y == 0 or 19, move the in the same direction of x and y.


    def reset(self, pos): #when game over and we restart the game, every thing will get reset..
        self.head = block(pos)
        self.boy_dir = []
        self.boy_dir.append(self.head)
        self.turns = {}
        self.dirX = 0
        self.dirY = 1


    def adding_block_to_snake(self):
        tail = self.boy_dir[-1]
        x_dir, y_dir = tail.dirX, tail.dirY

        if x_dir == 1 and y_dir == 0:
            self.boy_dir.append(block((tail.pos[0]-1,tail.pos[1]))) # tail.pos[0]-1 is left block of x axis, tail.pos[1] is y-axis
        elif x_dir == -1 and y_dir == 0:
            self.boy_dir.append(block((tail.pos[0]+1,tail.pos[1])))
        elif x_dir == 0 and y_dir == 1:
            self.boy_dir.append(block((tail.pos[0],tail.pos[1]-1)))
        elif x_dir == 0 and y_dir == -1:
            self.boy_dir.append(block((tail.pos[0],tail.pos[1]+1)))

        self.boy_dir[-1].dirX = x_dir #movement of new block should be in direction of the snake only
        self.boy_dir[-1].dirY = y_dir


    def draw(self, surface):  # this draw() func id to redirect to block class draw()
        for i, c in enumerate(self.boy_dir):
            if i ==0:
                c.draw(surface, True) # calling draw method of block class and TRUE is for eyes on head(i=0)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows #size of each grid in screen

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (0,0,0), (x,0),(x,w)) #horizontal lines- x:constant and y-variable
        pygame.draw.line(surface, (0,0,0), (0,y),(w,y)) #Vertical lines- y:constant and x-variable


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((67, 191, 199))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()


def Snake_food(rows, snake_object): # generating food for the snake at random positions..

    positions = snake_object.boy_dir

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: # if snake boy_dir position is equal to food position keep finding new position for food..
            continue
        else:     # else find position which is not equal to position of snake's boy_dir and food position, just break the loop and return the position (x, y)
            break

    return (x,y)


def message_box(subject, content): # message which will be displayed..when game get over..
    root = tk.Tk()
    root.attributes("-topmost", True) #this will pop up this window over the current running window..
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = pythonSnake((251, 255, 255), (10,10))  #(colour, position_of_pythonSnake)
    snack = block(Snake_food(rows, s), color=(127, 232, 23))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10) #10 frame/sec movement of snake
        s.move() #pythonSnake start move
        if s.boy_dir[0].pos == snack.pos: # when food touch the snake, it should be added as boy_dir part of snake
            s.adding_block_to_snake() # this function will actually add food to boy_dir..
            snack = block(Snake_food(rows, s), color=(127, 232, 23))

        for x in range(len(s.boy_dir)):  # when snake hit his body.. the game should be over..
            if s.boy_dir[x].pos in list(map(lambda z:z.pos,s.boy_dir[x+1:])):
                print('Score: ', len(s.boy_dir))
                score = len(s.boy_dir)*10
                message_box('You Lost!','Your Score: '+str(score))
                s.reset((10,10))
                break


        redrawWindow(win)


    pass



main()
