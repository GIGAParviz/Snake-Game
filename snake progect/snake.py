from turtle import Turtle

start_pososion = [(0 , 0) , (-20 , 0) , ( -40 , 0)]
snakemove = 20
class Snake:
    
    def __init__ (self):
        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]
        
    def creat_snake(self):
        for pos in start_pososion:   
            self.add_seg(pos)
     
    def add_seg(self , pos):
        newsection = Turtle("turtle")
        newsection.color("white")
        newsection.penup()
        newsection.goto(pos)
        self.segment.append(newsection)
           
            
    def extend(self):
        # ezaafe kardan be dome maar
        self.add_seg(self.segment[-1].pos())       
            
    def move(self):
        for segnum in range(len(self.segment) -1 , 0 , -1):
            new_x = self.segment[segnum - 1].xcor()
            new_y = self.segment[segnum - 1].ycor()
            self.segment[segnum].goto(new_x , new_y)                
        self.head.forward(snakemove)
        
        
        
    def up(self):
        self.head.setheading(90)
    
            
    def down(self):
        
        self.head.setheading(270)
            
    def left(self):
        
        self.head.setheading(180)
            
    def right(self):
        
        self.head.setheading(0)
        
        
        
    
        
        
    # self.segment[0].left(10)
    
    
# this is another way but preivios is better

# secsection = Turtle('square')
# secsection.color("white")
# secsection.goto(-20 , 0)

# thirssection = Turtle('square')
# thirssection.color("white")
# thirssection.goto(-40 , 0)
