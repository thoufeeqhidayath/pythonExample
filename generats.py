import collections
def counts(x):
    while(x>0):
        if(x%2==0):
            yield x
            x-=1
        else:
            x=x-1

print (list(counts(5)))
for i in counts(10):
    print i


