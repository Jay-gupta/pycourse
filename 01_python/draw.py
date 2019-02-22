import turtle

w = turtle.Screen()
x = turtle.Turtle()

for i in range(100):
    # if i % 2 == 0:
    #     print("draw")
    # else:
    #     print("dont")

    #print(i, i % 2);
    if i % 2 == 0:
        x.pendown()
    else:
        x.penup()

    x.forward(200)
    x.left(85)

w.mainloop()
