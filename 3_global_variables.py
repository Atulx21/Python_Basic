x="PAIN"                               #Global variable

def myfanc():
    x="GOD"
    print("Know "+x)

myfanc()   

print("This world shall know "+x)



y="GOOD"

def mychange():
    global y          #we can change the value of global variable inside the function
    y="best"

mychange()

print("You know who is "+y)