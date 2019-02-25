

openfile=open("/Users/Mubarak/Documents/temp/pyml/filereading/xas.csv","r")
str=openfile.read()
length=len(str)
lists=[]
for index in range(length):
    if (str[index]!='\n' or','):
        lists.append(str[index])
        print(str[index])
    elif (str[index]==','):
        print("")
    elif(str[index]=='/n'):
      lists.append("/n")

for x in range (len(lists)):
    print lists[x]

print(openfile.readline())
print(''.join(lists))

for x in range(5):
    print(x)



print(str)
