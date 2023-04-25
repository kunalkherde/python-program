from threading import local


x = "25"
def foo ():
    x=45
    print("inside x :",x)
def globalvariable():
    global x
    print("the value of globel x",x)
print("the value of  x" , x)
foo()
globalvariable()