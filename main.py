#imported all the classes
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Formatted the screem

screen = Screen()
screen.setup(600,600)
screen.bgcolor("hot pink")
screen.title("My Snake Game")
screen.tracer(0)


#Created objects from classes
snake = Snake()
food = Food()
score = Scoreboard()

#Initialized movement of snake through the keyboard
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
screen.listen()
speed = 0.1

#The loop that runs the game


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    score.keep_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset()


            # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.add_score()

            # Detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset()


screen.exitonclick()



















