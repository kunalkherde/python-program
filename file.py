f = open("data.txt","r")
print("mode of file",f.mode)
print("name of file ",f.name)
print("closed or not",f.closed)
f.read(2)
f.close()
print("")
print("closed or not",f.closed)

