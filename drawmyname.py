import turtle

# beállítja az lpszíneket és a kezdőpozíciót ----------
screen = turtle.Screen()
screen.bgcolor('black')
trtl = turtle.Turtle(shape="turtle")
trtl.pen(pencolor='red', pensize=5)
trtl.up()
trtl.setpos(25 - screen.window_width()/2, screen.window_height()/2 - 25)
trtl.down()
# ------------------------------------------------------

# Z
trtl.forward(100)
trtl.right(135)
trtl.forward(141)
trtl.left(135)
trtl.forward(100)

# pos
trtl.up()
trtl.forward(50)
trtl.down()

# O
trtl.circle(50)

# pos
trtl.up()
trtl.left(60)
trtl.forward(115)
trtl.right(150)
trtl.down()

# L
trtl.forward(100)
trtl.left(90)
trtl.forward(50)

#pos
trtl.up()
trtl.forward(30)
trtl.left(90)
trtl.down()

# I
trtl.forward(100)

turtle.done()