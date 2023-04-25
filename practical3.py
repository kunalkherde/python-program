a = int(input("enter the element you want :"))
list = []
for i in range(1,a+1):
    x = int(input("enter the element"))
    list.append(x)
    avg = sum(list)/a
print("average of the numbers is :",avg)