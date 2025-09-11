import math
import random

class Person:
    def __init__(self, name, pets) :
        self.name=name
        self.pets = pets
    
    def greeting(self) :
        print (f"Hello my name is {self.name} and I have {self.pets} pets.")
    
mia = Person("Mia",4)
#print(mia)
mia.greeting()

class ScoreKeeper:
    def __init__(self, score):
        self.score = score = 0
    
    def scoreNormal(self):
        self.score+=100
        print( self.score)
        
    def scoreBonus(self):
        self.score+=1000
        print( self.score)

hi = ScoreKeeper(9)
#print(hi)
hi.scoreNormal()
hi.scoreBonus()


class MagicEightBall:
    def __init__(self, replies):
        MagicEightBall.replies = replies
        
    def ask(self,question):
        print (self.replies[random.randint(0,len(MagicEightBall.replies)-1)])
    
five = MagicEightBall(["no","yes", "maybe"])
five.ask("how do you fix a lightbulb?")

class Rectangle:
    def __init__(self, base, height):
        Rectangle.base=base;
        Rectangle.height=height;
    
    def area(self):
        area=self.base*self.height
        print(f"area = {area}")
      
    def perimeter(self):
        perimeter=self.base*2+self.height*2
        print(f"perimeter = {perimeter}")
              
    def diagonal(self):
        diagonal=math.sqrt(self.base**2+self.height**2)
        print(f"diagonal = {diagonal}")

circle = Rectangle(3,4) 
circle.area()
circle.perimeter()
circle.diagonal()