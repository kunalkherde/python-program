lower = 100 
upper = 3000
def armstrong():
    for num in range(0,10001):
        sum = 0
        temp = num 
    while num>0:
        digit =temp%10
        sum += digit**3
        temp//= 10 
    if sum == num:
        print(num)
armstrong()


