from turtle import Turtle, Screen

#Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

#Creating initial segment
segment = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)
#Moving snake continously
game_is_on = True
while game_is_on:
    for seg in segment:
        seg.forward(20)

screen.exitonclick()