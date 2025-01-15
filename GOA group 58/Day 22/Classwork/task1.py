# Define a function called find_average that takes a list or set of numbers as input
def find_average(numbers):
    # Check if the list/set is empty. If it is, return 0 (to avoid division by zero)
    if len(numbers) == 0:
        return 0
    # Initialize a variable to store the sum of the numbers
    sum = 0
 # Iterate through each number in the list/set 'numbers'   
    for number in numbers:
        # Add the current number to the total sum
        sum += number
    # Calculate the average by dividing the sum by the number of elements
    average = sum / len(numbers)
    # Return the calculated average
    return average