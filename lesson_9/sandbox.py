# def multiplication_of_three(number):
# # Your code here
#     result = 1
#     for i in range(3):
#          result = result * (number % 10)
#          number = number // 10
#     print(result)

# multiplication_of_three(349)
# def multiplication_of_three(number):
#     result = 1
#     for i in range(3):
#         result *= number % 10  # Extract the last digit and multiply it to result
#         number = number // 10  # Remove the last digit
#     print(result)
#
# # Example usage:
# multiplication_of_three(349)

def sum_even_and_product_odd(arr):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1
    odd_found = False
#
# # Iterate through the array
#     for num in arr:
#         if num % 2 == 0:
#             sum_even += num
#         else:
#             product_odd *= num
#             odd_found = True
#
# # If no odd numbers are found, set product_odd to 0
#     if not odd_found:
#        product_odd = 0
#
#     return [sum_even, product_odd]
#
# # Example usage:
# arr = [1, 2, 3, 4]
# result = sum_even_and_product_odd(arr)
# print(result)
# def invert_list(arr):
#
#     inverted_list = []
#
#         # Iterate over each number in the input list
#     for num in arr:
#             # Invert the number and add it to the inverted_list
#         inverted_list.append(-num)
#
#     return inverted_list
#
#     # Example usage:
# input_list = [1, 5, -2, 4]
# output_list = invert_list(input_list)
# print(output_list)
def max_diff(arr):
    # Check if the list is empty
    if len(arr) == 0:
        return 0

    # Find the maximum and minimum values in the list
    max_val = max(arr)
    min_val = min(arr)

    # Calculate the difference
    difference = max_val - min_val

    return difference


# Example usage:
input_list = [3, 5, 9, 2]
output = max_diff(input_list)
print(output)