import turtle

turtle.setup(width= 600, height=600)
t=turtle.Turtle()
t.shape('turtle')
name = t.screen.textinput("NIM", "Name of first player:")
i = 0
for i in range(0, 4):
    t.fd(100)
    t.lt(90)
