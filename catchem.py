
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
            self.display(g) #make new position visible wherever we've moved


my_berry = Berry()
my_catcher = Catcher()
#game loop
while True:
    my_catcher.run()
    my_berry.run()
    if my_berry.x_position == my_catcher.x_position and my_berry.y_position == my_catcher.y_position:
        print("score!")
        sense.set_pixel(my_catcher.x_position, my_catcher.y_position, (20,20,20))
        sleep(1)
        my_berry = Berry()
    if my_berry.y_position == None:
        my_berry = Berry() #make new berry after each one drops
