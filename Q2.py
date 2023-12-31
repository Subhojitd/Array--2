def distributeCandies(candyType):
    max_candies = len(candyType)//2 # Maximum number of candies alice can eat
    unique_candies = len(set(candyType)) # Count the number of unique candy types

    # Return the minimum of unique candies and max_candiaes
    return min(unique_candies, max_candies)

candyType = [3,3,4,4,5,6]
max_diff_types = distributeCandies(candyType)
print(max_diff_types)