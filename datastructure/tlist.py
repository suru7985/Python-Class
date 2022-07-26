from turtle import*
speed('fastest')
colour=['red', 'green', 'yellow']#, 'blue','pink']

s = len(colour)
for i in range(500):
    c=colour[i% s]
    pencolor(c)
    forward(100)
    left(360/s)
    for j in range(s):
        forward(100)
        left(360/60)

mainloop()   