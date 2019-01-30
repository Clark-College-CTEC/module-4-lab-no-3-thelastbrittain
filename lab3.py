# Lab No. 3
# CTEC 121
# Benjamin Brittain

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    win.setCoords(0,0,3,3)

    

    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3

    circle1 = Circle(Point(1.5,.5),.5)
    circle1.setFill('blue')
    circle1.draw(win)

    circle2 = Circle(Point(1.5,1.4),.4)
    circle2.setFill('blue')
    circle2.draw(win)

    circle3 = Circle(Point(1.5,2.1),.3)
    circle3.setFill('blue')
    circle3.draw(win)

    #for my own convenience: snowman head is centered at 1.5, 2.1   top is 2.4, bottom 1.8  left 2.4 right 1.8

    # for i in range(10):
    #     click = win.getMouse()
    #     print(click)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    eye1 = Circle(Point(1.3,2.1),.05)
    eye1.setFill('black')
    eye2 = eye1.clone()
    eye2.move(.3,0)
    eye1.draw(win)
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = Polygon(Point(1.5,2.1), Point(1.25,2), Point(1.5, 2.0))
    nose.setFill('orange')
    nose.draw(win)




    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    hat = Rectangle(Point(1,2.4), Point(2,3))
    hat.setFill('black')
    hat.draw(win)


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    hatline = Rectangle(Point(.8,2.4), Point(2.2,2.5))
    hatline.setFill('black')
    hatline.draw(win)
    




    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()