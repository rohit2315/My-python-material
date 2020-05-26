def topten():
    yield 1
    yield 2

value=topten()

print(next(value))    
print(next(value))


# generators are basically used when we need to print a particular value 













def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq   #yield is the keyword wich converts it in generator rather than return
        n+=1

values=topten()        

for i in  values:
    print(i)   




nums=[5,4,3,2,8]
print(nums.sort())    