class person():
    def __init__(self , fname , lname ):
        self.fname = fname 
        self.lname = lname
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("kunal","kherde")
print(x.fname,x.lname)