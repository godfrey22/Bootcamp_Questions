# Setup an empty array to contain user input
input_array = []

# Initiate a loop to ask for numbers
while True:

    # Get the number
    user_input = input("Please input a number ('X' for exit)")

    # Exiting condition
    if user_input == 'X':
        break

    # Store the input
    try:
        # Determine if the input is a integer. 
        input_array.append(int(user_input))
    except ValueError:
        print("Please input a proper number")

# Initiate the counter and the variable to store the final result
counter = 1
sum_odd_pair = []
product_even_pair = []

# Iteration through the array
for number in input_array:
    for i in range(counter, len(input_array)):

        # Calculate the product and the sum of the pair
        number_product = number * input_array[i]
        number_sum = number + input_array[i]
        # If the product is even, print
        if(number_product%2 == 0):
            product_even_pair.append([number, input_array[i]])            
        # If the sum is odd, print
        if(number_sum%2 == 1):
            sum_odd_pair.append([number, input_array[i]])
    counter += 1

# Format the pairs and print
print("=====================")
print("Pairs that sum is odd:")
print(sum_odd_pair)
print("=====================")
print("Pairs that product is even:")
print(product_even_pair)        
print("=====================")
