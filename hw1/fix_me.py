'''
This is the first homework with using linters
'''


def calculate_average(numbers):
    '''Takes in nums array, returns the average of numbers'''
    total = sum(numbers)
    count = len(numbers)
    return total / count


nums = [10, 15, 20]
RESULT = calculate_average(nums)
print("The average is:", RESULT)
