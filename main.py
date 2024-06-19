from tkinter import *
from Ball import *
import time
import random

window = Tk()
window.geometry("600x500")
window.title("Multiple Animations")

WIDTH = 600
HEIGHT = 500
xvelocity = 2
yvelocity = 2

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

imgX = random.randrange(1,599)
imgY = random.randrange(1,499)


soccerBall = Ball(canvas, 2, 5, 120, 2, 3, 'white')
hockeyBall = Ball(canvas, 3, 4, 20, 4, 2, 'lightBlue')
volleyBall = Ball(canvas, 3, 4, 80, 3, 1, 'green')
basketBall = Ball(canvas, 3, 4, 100, 6, 2, 'orange')


while True:
    soccerBall.move()
    hockeyBall.move()
    volleyBall.move()
    basketBall.move()
    window.update()
    time.sleep(0.01)


window.mainloop()