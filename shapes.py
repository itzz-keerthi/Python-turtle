'''TASK
TO PRINT VARIOUS SHAPES FROM TRIANGLE TO DECAGON USING PYTHON TURTLE'''

import turtle
t1= turtle.Turtle()
t1.forward(60)
for i in range(1,4):
    t1.left(120)
    t1.forward(60)
t1.left(90)
t1.forward(60)

for i in range(1,3):
    t1.left(90)
    t1.forward(60)
t1.left(90)
t1.forward(60)
for i in range(1,5):
    t1.left(72)
    t1.forward(60)
    
t1.left(72)   
t1.forward(60)
for i in range(1,6):
    t1.left(60)
    t1.forward(60) 
    
t1.left(60)   #heptagon
t1.forward(60)
for i in range(1,7):
    t1.left(52)
    t1.forward(60)     
    
t1.left(52)   #octagon
t1.forward(60)
for i in range(1,8):
    t1.left(45)
    t1.forward(60) 
    
t1.left(45)   #nonagon
t1.forward(60)
for i in range(1,9):
    t1.left(40)
    t1.forward(60) 
     
    
t1.left(40)   
t1.forward(60)
for i in range(1,11):
    t1.left(36)
    t1.forward(60)

    
turtle.mainloop()
