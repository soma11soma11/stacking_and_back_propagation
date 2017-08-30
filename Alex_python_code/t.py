print("dshfkj")
print((-1)**4)
import turtle

#turtle.forward(60); turtle.left(90); turtle.forward(60);

#for i in range(10):
    #for cod in "Yo", "mama":
     #print(i)
     #print("Me" + cod)

def Shape(length, arms,sides,sign):
    if sign*sign != 1:
     print("Wrong sign dumbass")
    else:    
       for i in range(arms):
        turtle.right((sign*360)/(sides))
        turtle.forward(length)

for i in range (2,12):
    Shape(100,7,6,1)
    turtle.left(360/3)
    
   # if (i % 2==1):
    # turtle.left(360/3)
    #else:
      #  tur
    # turtle.left(360/6)
