li=[12,3,46,58]
print(li[2])

it=iter(li) #iter function 
print(it.__next__())# this will preserve the previous value
print(it.__next__())
print(next(it))# another way of writing

class Topten:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:   #here have to mention the stop point
            val=self.num
            self.num+=1

            return val

        else:
            raise StopIteration   # else condition make sure that iteration stops if it goes beyond 10

value=Topten()

for i in value:
    print(i)            

