
from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class Snake:
    pass

class Food:
    pass
def next_turn():
    pass

def change_direction(new_direction):
    pass


def check_collision():
    pass

def game_over():
    pass


window = Tk()
window.title("Snake")
window.resizable(True, True)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=("Consolas", 28, "bold"))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()


#https://www.youtube.com/watch?v=XKHEtdqhLK8
#11:34:48