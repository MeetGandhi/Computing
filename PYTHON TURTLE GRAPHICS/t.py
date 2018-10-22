l=input()
n=input()
s=input()
import turtle
t=turtle.Turtle()
for j in range(n):
    for i in range(s):
        t.forward(l)
        t.left(360/s)
    t.forward(l)
    t.left(360/n)
turtle.done()
