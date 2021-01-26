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
        self.y_position = self.y_position + 1

    def display(self,color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def run(self):
        r  = (255,200,21)
        self.display(r)  #display new pixel
        time.sleep(1)
        K = (0,0,0)
        self.display(k) #erase last pixel
        self.move()





my_berry = Berry()

#game loop
while True:

    my_berry.run()
