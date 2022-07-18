import turtle as tt
from Agent import *


DIR_UP    = 0
DIR_RIGHT = 1
DIR_DOWN  = 2
DIR_LEFT  = 3

WALL = -1
EMPTY = 0

#  ^ 
#< R > 
#  v 
# 
# 

# penalties
PEN_OUTSIDE = -2
PEN_WALL    = -1
PEN_TURN  = -0.5
PEN_WALK    = 0


class Enviroment:
#                                    x|y        /          x|y      /     dir 
    def __init__(self, room_size = (10,10), robo_coords = [5,5],robo_dir = DIR_DOWN):

        self.room_size = room_size
        self.room_sectors = [
            [
                EMPTY for x in range(self.room_size[0])
            ]   for y in range(self.room_size[1])
            
        ]
        self.room_sectors[7][5] = WALL
        self.room_sectors[7][6] = WALL
        self.room_sectors[7][7] = WALL
        

        self.robo_coords = robo_coords
        self.robo_dir = robo_dir

        self.scale = 50 # pixels/coords

    def coordsToPixels(self,coords):
        sx, sy = self.room_size
        x,y = coords
        scrx = ( x - sx / 2) * self.scale
        scry = -(y -sy / 2 ) * self.scale
        return [scrx,scry]  
    
    def render(self):
        draw = tt.Turtle()
        screen = tt.Screen()
        screen.setup(self.room_size[0] * self.scale, self.room_size[1] * self.scale)

    #  squares
        tt.tracer(0,0)
        
        for y in range (self.room_size[1]):
            for x in range (self.room_size[0]):
                draw.penup()
                draw.goto(self.coordsToPixels((x,y)))
                draw.pendown()
                color = 'white'
                if self.room_sectors[y][x] == WALL:
                    color = 'gray'

                draw.fillcolor(color)
                draw.begin_fill()
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.end_fill() 



        # adjust  starting point robot
        robot_screen_coords = self.coordsToPixels(self.robo_coords)
        robot_screen_coords[1] -= self.scale
        robot_screen_coords[0] += self.scale / 2
        draw.penup()
        draw.goto(robot_screen_coords)
        draw.pendown()
        draw.fillcolor('gray')
        draw.begin_fill()
        draw.circle(self.scale/2)
        draw.end_fill()

    #   Direction moving    
        if self.robo_dir ==  DIR_DOWN:
            draw.left(90)
            draw.forward(10)
            draw.right(90)
            draw.forward(10)
            draw.left(90)

        if self.robo_dir ==  DIR_UP:
            draw.penup()
            draw.left(90)
            draw.forward(28)
            draw.right(90)
            draw.pendown()
        
        if self.robo_dir ==  DIR_RIGHT:
            draw.penup()
            draw.left(90)
            draw.forward(25)
            draw.right(90)
            draw.forward(22)
            draw.left(90)
            draw.pendown()
        
        if self.robo_dir ==  DIR_LEFT:
            draw.penup()
            draw.left(90)
            draw.forward(25)
            draw.left(90)
            draw.forward(22)
            draw.left(90)
            draw.pendown()



        
    #  small circle
        draw.fillcolor('green')
        draw.begin_fill()
        draw.circle(10)
        draw.end_fill()
        
        tt.hideturtle()
        draw.hideturtle()
        tt.update()
        #tt.done()
        #input()
    



    def actDir(self):
        if self.robo_dir == DIR_UP:
            self.robo_coords[1] -= 1    
        if self.robo_dir == DIR_RIGHT:
            self.robo_coords[0] += 1
        if self.robo_dir == DIR_DOWN:
            self.robo_coords[1] += 1
        if self.robo_dir == DIR_LEFT:
            self.robo_coords[0] -= 1
    
    
    def step(self,action):
        pen = PEN_WALK
        if action == ACT_RIGHT:
            self.robo_dir += 1
            if self.robo_dir > 3:
                self.robo_dir = 0
    
        
        # HW 6 * : try to optimize this code 
        #   hint : try to set a sign variable 
        #   hint : try to use dict or list with predefinited directrion



        if action == ACT_FRONT:
            self.actDir()

        if action == ACT_BACK:
            self.actDir()
        
        if action == ACT_LEFT:
            self.actDir()    
        
        if action == ACT_RIGHT:
            self.actDir()

        

        # if action == ACT_FRONT:
        #     self.robo_dir = DIR_RIGHT
        #     self.robo_coords[0] += 1

        # if action == ACT_BACK:
        #     self.robo_dir = DIR_LEFT
        #     self.robo_coords[0] -= 1

        # if action == ACT_LEFT:
        #     self.robo_dir = DIR_UP
        #     self.robo_coords[1] -= 1

        # if action == ACT_RIGHT:
        #     self.robo_dir = DIR_DOWN
        #     self.robo_coords[1] += 1
        

        
        if self.robo_coords[0] >= self.room_size [0] or\
           self.robo_coords[1] >= self.room_size [1] or\
           self.robo_coords[0]< 0 or\
           self.robo_coords[1] < 0:
               pen = PEN_OUTSIDE
        
        elif self.room_sectors[self.robo_coords[1]][self.robo_coords[0]] == WALL:
            pen = PEN_WALL

        state = [
            self.robo_coords,
            self.robo_dir,
            pen
        ]


        return state

        










