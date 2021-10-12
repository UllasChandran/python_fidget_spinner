import turtle 
win = turtle.Screen()
win.bgcolor("black")
win.setup(700,700)
win.title("Fidget Spinner")
turtle.color("Yellow")
turtle.write("FIDGET SPINNER" , align= "right" , font=("Arial" , 20 , "bold") )
turtle.color("Orange")
turtle.write("USE SPACE BUTTON TO SPEED UP " , align= "left" , font=("Arial" , 15 , "bold") )



obj1 = turtle.Turtle()
obj1.speed(8)
obj1.color("white")
obj1.width(3)
obj1.hideturtle()
win.tracer(False)
speed=[0] 
length = 100
rad = 120
dot_rad = 30 
angle = 0
dot = 5
obj1.goto(0.00 , -200.00)
obj1.right(angle)
obj1.forward(length)
obj1.dot(rad , "red")
obj1.dot(dot,"yellow")
obj1.back(length)
obj1.right(90)


obj1.right(angle)
obj1.forward(length)
obj1.dot(rad , "green")
obj1.dot(dot,"yellow")
obj1.back(length)
obj1.right(90)


obj1.right(angle)
obj1.forward(length)
obj1.dot(rad , "blue")
obj1.dot(dot,"yellow")
obj1.back(length)
obj1.right(90)


obj1.right(angle)
obj1.forward(length)
obj1.dot(rad , "indigo")
obj1.dot(dot,"yellow")
obj1.back(length)
obj1.right(90)









def spinner():
    obj1.clear()
    angle = speed[0]/10
    obj1.goto(0.00 , -200.00)
    obj1.right(angle)
    obj1.forward(length)
    obj1.dot(rad , "red")
    obj1.dot(dot_rad,"yellow")
    obj1.back(length)
    obj1.right(90)


    obj1.right(angle)
    obj1.forward(length)
    obj1.dot(rad , "green")
    obj1.dot(dot_rad,"yellow")
    obj1.back(length)
    obj1.right(90)


    obj1.right(angle)
    obj1.forward(length)
    obj1.dot(rad , "blue")
    obj1.dot(dot_rad,"yellow")
    obj1.back(length)
    obj1.right(90)


    obj1.right(angle)
    obj1.forward(length)
    obj1.dot(rad , "indigo")
    obj1.dot(dot_rad,"yellow")
    obj1.back(length)
    obj1.right(90)




def speedingup():
    speed[0]  += 25 
def  roatate():
    if speed[0] !=0 :
        speed[0] -= 1
    spinner()
    win.ontimer(roatate,20)
def main():
    win.tracer(False)
    win.listen()
    win.onkey(speedingup,'space')
   
    roatate()
    
    
    turtle.done()

if __name__=="__main__":  
    main()
