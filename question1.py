# Read a list of integers from user input.

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

print(input_array)