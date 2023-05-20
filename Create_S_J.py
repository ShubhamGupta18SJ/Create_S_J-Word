from turtle import*
color('cyan')
bgcolor('black')   # Print S
speed(0)
right(370)

for n in range(65):
    circle(30)
    if 3 < n :
        left(5)
         
    if 40< n :
        right(15)
        circle(30)
    if n < 65:
        forward(10)
    else:
        forward(5)
        pass
        

color('cyan')
bgcolor('black')
speed(0)         #Print J
up()
goto(200,300)
down()
right(27)
for n in range(60):
    circle(30)
      
    if 28< n :
        right(6)
        
    if n < 75:
        forward(10)
    else:
        forward(5)
      
