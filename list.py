from time import process_time


n = int(input("Enter the numbers : "))
l = []
for i in range(0,n):
    element = int(input("Enter an Element : "))
    l.append(element)
print(l)
d= int(input("Enter the element for delte :"))
l.remove(d)
print(l)
print("Sorted list")
l.sort()
print("list=",l)
print("Rrverse List ")
l.reverse()
print("list",l)
l.count(12)
print("count :",l)