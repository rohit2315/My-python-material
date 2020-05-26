def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=temp

nums=[5,4,3,2,8]
sort(nums)
print(nums)                


nums=[5,4,3,2,8]
nums.sort()
print(nums)
