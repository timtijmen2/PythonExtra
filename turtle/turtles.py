import turtle             
import time
colors = [ "red","purple","blue","green","orange","yellow"]
turtle.speed(0)
pen = turtle.Pen()
turtle.bgcolor("pink")
i = 0
times = 0
turtle.width(10)
positie = turtle.pos()
print(positie)
for x in range(360):
    turtle.color(colors[x % 6])
    turtle.right(i)
    turtle.forward(100)
    i += 5
    times += 1
    print(times)
    if times == 144:
        turtle.right(90) 
turtle.done()





##   my_pen.pencolor(colors[x % 6])
##   my_pen.width(x/100 + 1)
##   my_pen.forward(x)
##   my_pen.left(59)
   
##turtle.done()