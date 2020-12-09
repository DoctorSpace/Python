import turtle

directions = 'R'
intations = 3
line_length = 100
angle = 90

turtle.penup()
turtle.setpos(0, 0)
turtle.width(20)
turtle.pendown()

for i in range(intations):
    rev = directions[::-1]
    rev = rev.replace('R', '-'.replace('L','R').replace('-','L'))
    directions = directions + 'R' + rev

for a in directions:
    if a=='R':
        turtle.right(angle)
    else:
        turtle.left(angle)
    turtle.forward(line_length)

turtle.update()
turtle.done()