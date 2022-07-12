from tkinter import LEFT, RIGHT
import turtle as tt


UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3
class Enviroment:
    #
    def __init__(self, room_size = (10,10), robo_coords = (5,5),robo_dir =UP):

        self.room_size = room_size

        self.robo_coords = robo_coords
        self.robo_dir = robo_dir

        self.scale = 50

    def coordsToPixels(self,coords):
        sx, sy = self.room_size
        x,y = coords
        scrx = ( x - sx / 2) * self.scale
        scry = -(y -sy / 2 ) * self.scale
        return[scrx,scry]  
    
    def render(self):
        screen = tt.Screen()
        screen.setup()
        screen.setup(self.room_size[0] * self.scale, self.room_size[1]* self.scale)

#       vertical grid lines
        tt.tracer(0,0)
        tt.right(90)
        for x in range(self.room_size[0]):
            tt.penup()
            tt.goto(self.coordsToPixels((x,0)))
            tt.pendown()
            tt.forward(self.room_size[1] * self.scale)

        tt.penup()
        tt.goto(self.coordsToPixels((0,0)))
        tt.left(90)
 
 #       horizontal grid lines

        for y in range(self.room_size[1]):
            tt.penup()
            tt.goto(self.coordsToPixels((0,y)))
            tt.pendown()
            tt.forward(self.room_size[0] * self.scale)
        
        robot_screen_coords = self.coordsToPixels(self.robo_coords)
        robot_screen_coords[1] -= self.scale
        robot_screen_coords[0] += self.scale /2
        tt.penup()
        tt.goto(robot_screen_coords)
        tt.pendown()
        tt.fillcolor('gray')
        tt.begin_fill()
        tt.circle(self.scale/2)
        tt.end_fill()

        if self.robo_dir ==  DOWN:
            tt.left(0)

        if self.robo_dir ==  UP:
            tt.penup()
            tt.left(90)
            tt.forward(28)
            tt.right(90)
            tt.pendown()
        
        if self.robo_dir ==  RIGHT:
            tt.penup()
            tt.left(90)
            tt.forward(25)
            tt.right(90)
            tt.forward(22)
            tt.left(90)
            tt.pendown()
        
        if self.robo_dir ==  LEFT:
            tt.penup()
            tt.left(90)
            tt.forward(25)
            tt.left(90)
            tt.forward(22)
            tt.left(90)
            tt.pendown()


#       small circle
        tt.fillcolor('green')
        tt.begin_fill()
        tt.circle(10)
        tt.end_fill()
        tt.hideturtle()

        tt.update()
        tt.done()
        
        input()
