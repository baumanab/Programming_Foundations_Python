# import statements

import turtle

'''
doc string
'''

def draw_square():
	'''
	draws a draw_square
	'''
	
	# set up window
	window = turtle.Screen()
	window.bgcolor('red')


	# assign attributes
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('blue')

	# draw the square
	sides = 4
	sides_count = 0

	while(sides_count < sides):

		brad.forward(100)    

		## turn at right angle

		brad.right(90)
		sides_count += 1

	## close window on click
	window.exitonclick()

	
draw_square()

