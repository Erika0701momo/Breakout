from turtle import Turtle
colors = ["yellow", "red", "blue", "green", "orange", "pink"]

class BlockManager():
    def __init__(self):
        self.blocks = []
        self.removed_blocks = []
        self.x = -275
        self.y = 80
    def create_blocks(self):
        for color in colors:
            for n in range(13):
                block = Turtle()
                block.shape("square")
                block.color(color)
                block.shapesize(stretch_wid=1, stretch_len=2)
                block.penup()
                block.goto(self.x, self.y)
                self.blocks.append(block)
                self.x += 45
            self.x = -275
            self.y += 25