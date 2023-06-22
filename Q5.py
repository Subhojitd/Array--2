def maximumProduct(nums):
    nums.sort() # Sort the array in ascending order 
    n = len(nums)
    # Maximum product can be acheived by either multiplying the three largest elements or two smallest and one largest element
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1]*nums[n-1]) 

nums = [5,4,3,2,1]
max_product = maximumProduct(nums)
print(max_product)