a = int(input("enter the number : "))
print("the factorial is")
first_num = 0
second_num = 1
for i in range(0,a):
    if(i<=1):
        n =i
    else:
        n= first_num+ second_num
        first_num = second_num
        second_num = n
    print(n)