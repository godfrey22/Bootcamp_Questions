import random

# 2. Find all pairs of numbers in the list whose product is even and whose sum is odd.

# Initiate an empty array
number_pairs = []
# Generate 10 pairs of random int
for i in range(10):
    cache = [random.randint(0,100), random.randint(0,100)]
    number_pairs.append(cache)

# Initiate iteration to iterate through the array
for number_pair in number_pairs:
    # Calculate the product and sum
    number_product = number_pair[0] * number_pair[1]
    number_sum = number_pair[0] + number_pair[1]

    # If the product is even, print
    if(number_product%2 == 0):
        print("number %d and number %d's product is %d"%(number_pair[0], number_pair[1], number_product))
    
    # If the sum is odd, print
    if(number_sum%2 == 1):
        print("number %d and number %d's sum is %d"%(number_pair[0], number_pair[1], number_sum))

