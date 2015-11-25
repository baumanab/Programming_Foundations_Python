# import dependencies

import turtle

def draw_square(some_turtle):
	'''
	accepts an instance of turtle
	and returns a square drawn 
	by that turtle
	'''

	# draw the square
	sides = 4
	sides_count = 0

	while(sides_count < sides):

		some_turtle.forward(100)    

		## turn at right angle

		some_turtle.right(90)
		sides_count += 1

def draw_art():
	'''
	Sets up canvas for turtle to 
	draw on and sets up turtle attributes
	'''
	# set up windows
	window = turtle.Screen()
	window.bgcolor('red')

	# create an instance of a turtle and draw square
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('yellow')
	brad.speed(2)

	# pass turtle instance to draw_square function
	draw_square(brad)

	# close canvas on clickity

	window.exitonclick()

draw_art()
