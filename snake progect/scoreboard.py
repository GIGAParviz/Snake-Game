from turtle import Turtle   

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0 , 270)
        self.write(f"امتیاز: {self.score}" , align="center" , font=("Arial" , 20 , "normal"))

        self.hideturtle()
        
        
    def update_scoreboard(self):
        self.write(f"امتیاز: {self.score}" , align="center" , font=("Arial" , 20 , "normal"))
        

        
    def game_over(self):
        self.goto( 0 , 0 )
        self.write(f"گند زدی، مثل زندگیت سریع خودتو بکش" , align="center" , font=("Arial" , 24 , "normal"))
        self.goto( 0 , -15 )
        self.write(f"Created By Amir Mehdi Parviz", align="center" , font=("Arial" , 10 , "normal"))
 
        
    
        
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       