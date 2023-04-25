baby =0
school=0
adult =0
for i in range (1,6):
    n = int(input("Enter the age :"))
    if n<=3:
        baby += 1
    elif (n<=10):
        school +=1
    else:
        adult +=1
print("baby age :",baby)
print("school age :",school)
print("adult age :",adult)