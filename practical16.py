def factors(a):
    print("the factors of ",a,"are :")
    for i in range (1,a+1):
        if a%i==0:
            print(i)
b = int(input("Enter the number :"))
factors(b)
