def search(nums,target):
    left =0
    right = len(nums)-1

    while left<= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
        
    return -1

nums =[1,7,8,3,4,9,34]
target=9
index= search(nums,target)
print(index)
