from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 600 , height = 600)
screen.bgcolor("black")
screen.title("بازی مار")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")
    
start_pososion = [(0 , 0) , (-20 , 0) , ( -40 , 0)]

segment = []

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)     
    snake.move()
    
   #tashkhis barkhoor ba ghazaa(food detect)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #tashkhis barkhoord ba divaar   
    if snake.head.xcor() > 280  or  snake.head.xcor() < -280 or  snake.head.ycor() > 280 or  snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over() 
    
    #tashkhis barkhoord ba dom
    for segment in snake.segment:
        
        if segment == snake.head:
            pass
        
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  
            
        

# this is another way but preivios is better

# secsection = Turtle('square')
# secsection.color("white")
# secsection.goto(-20 , 0)

# thirssection = Turtle('square')
# thirssection.color("white")
# thirssection.goto(-40 , 0)




screen.exitonclick()