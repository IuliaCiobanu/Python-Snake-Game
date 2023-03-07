from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Julia is coding a Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increse_score()

    for segment in snake.segments[1:]:
        # if snake.segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.end_the_game()
            game_is_on = False

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.end_the_game()


screen.exitonclick()
