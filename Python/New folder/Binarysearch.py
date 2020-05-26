# in binary search we search values by narrowing the range of values by taking the midpoints between lower and upperbound values
#unlike linear search where we have to iterate through all values it takes time when the list is too large we 
#use binary search which saves time by narrowing the range of number
# In binary we have to keep the number in sorted way like in ascending or descendding order by using list.sort

pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1  # it means we will have to search right of mid element so low will be next of mid

                
            else :
                
                u-=1   # it means we have to seaarch left of mid element

    return False
s
list=[5,26,95,157,1098,52345,65978] 
n=1153
if search(list,n):
    print('Found at',pos)

else:
    print('Not Found')                   
