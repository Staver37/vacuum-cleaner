import turtle as tt

DIR_UP    = 0
DIR_RIGHT = 1
DIR_DOWN  = 2
DIR_LEFT  = 3
draw = tt

    #   Direction moving    

# if robo_dir ==  DIR_UP:
#     draw.penup()
#     draw.left(90)
#     draw.forward(28)
#     draw.right(90)
#     draw.pendown()

# if robo_dir ==  DIR_RIGHT:
#     draw.penup()
#     draw.left(90)
#     draw.forward(25)
#     draw.right(90)
#     draw.forward(22)
#     draw.left(90)
#     draw.pendown()

# if robo_dir ==  DIR_DOWN:
#     draw.left(90)
#     draw.forward(10)
#     draw.right(90)
#     draw.forward(10)
#     draw.left(90)

# if robo_dir ==  DIR_LEFT:
#     draw.penup()
#     draw.left(90)
#     draw.forward(25)
#     draw.left(90)
#     draw.forward(22)
#     draw.left(90)
#     draw.pendown()

PU   = draw.penup()
PD   = draw.pendown()
F25  = draw.forward(25)
F22  = draw.forward(22)
F10  = draw.forward(10)
L90  = draw.left(90)
R90  = draw.right(90)

PU  =  1
PD  =  2
F25 =  3
F22 =  4
F10 =  5
L90 =  6 
R90 =  7

robo_dir = 1

SMOL_CIRC_DIR= [
      
        [  1, 6, 3, 6, 2 ],                    # 0
        [  1,  7, 3, 7, 3, 4, 6], # 1
        [  L90,  F10, R90, F10,L90 ],          # 2
        [ PU, L90, F25, L90, F22, L90, PD ]    # 3
              ]
if robo_dir == [0] or [1] or [2] or 3:
    SMOL_CIRC_DIR = robo_dir
    print(SMOL_CIRC_DIR)