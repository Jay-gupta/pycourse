import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


w = turtle.Screen()
x = turtle.Turtle()

for _ in range(10):
    draw_square(turtle, 100)
    turtle.left(10)

w.mainloop()
