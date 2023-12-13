import turtle

ventana = turtle.Screen()
ventana.title("Mi ventana de Turtle")
ventana.bgcolor("white")
mi_tortuga = turtle.Turtle()

mi_tortuga.goto(-100, -100)
#dibujando base
mi_tortuga.fillcolor('yellow')
mi_tortuga.color('black', 'yellow')
mi_tortuga.width(3)
mi_tortuga.speed(5)

mi_tortuga.begin_fill()
for _ in range(4):
    mi_tortuga.forward(200)
    mi_tortuga.left(90)
mi_tortuga.end_fill()

#Dibujando un ojo
mi_tortuga.goto(-60, 30)

mi_tortuga.fillcolor('blue')
mi_tortuga.color('black','cyan')
mi_tortuga.width(4)
mi_tortuga.speed(5)

mi_tortuga.begin_fill()

# Dibujar el rectángulo
longitud_lado_1 = 40
longitud_lado_2 = 40

for _ in range(2):
    mi_tortuga.forward(longitud_lado_1)
    mi_tortuga.left(90)
    mi_tortuga.forward(longitud_lado_2)
    mi_tortuga.left(90)

mi_tortuga.end_fill()
mi_tortuga.penup()

#Dibujando el otro ojo

mi_tortuga.goto(20, 30)

mi_tortuga.pendown()
mi_tortuga.fillcolor('blue')
mi_tortuga.color('black','cyan')
mi_tortuga.width(4)
mi_tortuga.speed(5)

mi_tortuga.begin_fill()

for _ in range(2):
    mi_tortuga.forward(longitud_lado_1)
    mi_tortuga.left(90)
    mi_tortuga.forward(longitud_lado_2)
    mi_tortuga.left(90)

mi_tortuga.end_fill()
mi_tortuga.penup()

#Dibujando boca
mi_tortuga.goto(-80, -50)
mi_tortuga.pendown()

mi_tortuga.pendown()
mi_tortuga.fillcolor('blue')
mi_tortuga.color('black', 'cyan')
mi_tortuga.speed(5)

longitud_lado_1 = 160
longitud_lado_2 = 40

mi_tortuga.begin_fill()

for _ in range(2):
    mi_tortuga.forward(longitud_lado_1)
    mi_tortuga.left(90)
    mi_tortuga.forward(longitud_lado_2)
    mi_tortuga.left(90)

mi_tortuga.end_fill()

turtle.mainloop()