import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            is_game_on = False
            scoreboard.game_over()




screen.exitonclick()