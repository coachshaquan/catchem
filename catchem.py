
#Classes - first half of day

#Detecting Input - second half if we get to it
from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()



class Berry:
    def __init__(self):
        self.x_position = random.randint(0,7)
        self.y_position = 0

    def move(self):
        if self.y_position>=0 and self.y_position <=7:
            self.y_position = self.y_position + 1
        else:
            self.y_position = None #now our berry can no longer be touched

    def display(self,color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def run(self):
            r = (255, 200, 21)
            self.display(r) #display new pixel
            sleep(1)
            k = (0,0,0)
            self.display(k) #erase last pixel
            self.move()


class Catcher:
    def __init__(self):
        self.x_position = random.randint(0,7)
        self.y_position = 7
        g = (0, 255, 0)
        self.display(g)

    def display(self,color):
        sense.set_pixel(self.x_position, self.y_position, color)

    #direction: 1 for right, -1 for left
    def move(self,direction):
        self.x_position = self.x_position + direction


    def run(self):

        for event in sense.stick.get_events():
            k = (0,0,0)
            g = (0, 255, 0) #green
            self.display(k) #clear previous position
            if event.action == "pressed" and event.direction == "left":
                self.move(-1) #move left
            elif event.action == "pressed" and event.direction == "right":
                self.move(1) # move right
            self.display(r) #make new position visible wherever we've moved


berry = Berry()
catcher = Catcher()
#game loop
while True:
    catcher.run()
    berry.run()
    if berry.x_position == catcher.x_position and berry.y_position == catcher.y_position:
        print("score!")
        sense.set_pixel(catcher.x_position, catcher.y_position, p)
        sleep(1)
        berry = Berry()
    if berry.y_position == None:
        berry = Berry() #make new berry after each one drops
