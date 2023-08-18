from tkinter import *
import random

GAME_WIDTH = 1750
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#66FF66"
FOOD_COLOR = "#FF6666"
BACKGROUND_COLOR = "#333333"
GAME_OVER_COLOR = "#FF0000"
GAME_OVER_TEXT_COLOR = "#FFFFFF"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        score_label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def reset_game():
    global score, direction, snake, food                      
    score = 0
    direction = 'down'
    score_label.config(text="Score:{}".format(score))

    snake = Snake()
    food = Food()

def space_pressed(event):
    global snake, food

    if canvas.find_withtag("gameover"):
        canvas.delete("gameover")
        reset_game()  # Call reset_game instead of next_turn
        next_turn(snake, food)


def game_over():
    
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2, canvas.winfo_height() / 2,
        font=('consolas', 70), text="GAME OVER", fill=GAME_OVER_COLOR, tag="gameover"
    )
    canvas.create_text(
        canvas.winfo_width() / 2, canvas.winfo_height() / 1.5,
        font=('consolas', 20), text="Press Space to Play", fill=GAME_OVER_TEXT_COLOR, tag="gameover"
    )


window = Tk()
window.title("Snake game")
window.resizable(False, False)


score = 0
direction = 'down'

score_label = Label(window, text="Score:{}".format(score), font=('consolas', 24), fg='white', bg=BACKGROUND_COLOR)
score_label.pack()


canvas = Canvas(
    window, bg=BACKGROUND_COLOR, highlightthickness=0, height=GAME_HEIGHT, width=GAME_WIDTH
)
canvas.pack()



window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<space>', space_pressed)  # Bind space bar key press

snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()