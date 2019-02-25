import collections
str="new laptop have laptop with more than 3 keys"
list=str.split()
print list

hashMap={}
for element in list:
    if element not in hashMap:
        hashMap[element]=1
    else:
        hashMap[element] =  hashMap[element]+1
print hashMap

