from collections import Counter

def findLHS(nums):
    num_counts = Counter(nums) # Count the occurance of each number

    max_length =0
    for num in num_counts:
        if num + 1 in num_counts:
            # If the current number and its adjacent number exist in the array 
            # Update the max_length with the count of the harmonious subsequence
            max_length=max(max_length,num_counts[num] + num_counts[num+1])

    return max_length
    

nums=[1,3,2,2,5,2,3,7]
longest_subseq_length = findLHS(nums)
print(longest_subseq_length)