n = int(input("Enter the number :"))
sum = 0
temp = n
while(n>0):
    digit=n%10
    sum += digit**3
    n //= 10
if (sum==temp):
    print("it is a armstrong number :")
else:
    print("it is not armstrong number:")