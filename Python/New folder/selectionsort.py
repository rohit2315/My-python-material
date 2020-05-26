def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,5):
            if nums[j]<nums[minpos]:
                minpos=j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp  

        print(nums) # see one by one


nums=[5,3,6,8,2] 
sort(nums)
print(nums)            
