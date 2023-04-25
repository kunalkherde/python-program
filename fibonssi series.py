a = int(input("enter the number : "))
x = 0
y= 1
for i in range (0,a):
    if (i<=1):
        n=i
    else:
        n=x+y
        x=y
        y=n
    print(n)