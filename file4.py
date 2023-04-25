f = open("data.txt","r")
data = f.read()
words = data.split()
print("the length of the words:" , len(words))