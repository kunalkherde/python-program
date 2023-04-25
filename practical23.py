class complex:
    def complex (self):
        self.realpart = int(input("Enter the real part"))
        self.imaginarypart = int(input("Enter the imaginary part"))
    def display(self):
        print(self.realpart,"+",self.imaginarypart,"i",sep="")
    def sum(self,c1,c2):
        self.realpart = c1.realpart+ c2.realpart
        self.imaginarypart = c1.imaginarypart + c2.imaginarypart
    def diff(self,c1,c2):
        self.realpart = c1.realpart- c2.realpart
        self.imaginarypart = c1.imaginarypart - c2.imaginarypart

    c1 = complex()
    c2 = complex()
    c3 = complex()
    print("Enter 1st complex number")
    c1.initcomplex()
    print("Enter 2nd complex number")
    c2.initcomplex()
    print("Enter 1st complex number :",end="")
    c1.display()
    print("Enter 2nd complex number :",end="")
    c2.display()
    print("Sum of the given complex number :")
    c3.sum(c1,c2)
    c3.display
    print("difference of the given complex number :")
    c3.diff(c1,c2)
    c3.display()




