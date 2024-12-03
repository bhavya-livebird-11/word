from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
 
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)         # does not show changes show only when screen update
game_is_on = True


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Move The  Snake
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with tail.
    #if head collides with any segment in the tail
    # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()