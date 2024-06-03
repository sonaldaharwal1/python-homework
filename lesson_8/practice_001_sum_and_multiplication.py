# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24

input_list =1,2,3,4
sum_result =0
mul_result = 1
print(sum(input_list))
for num in input_list:
    mul_result *= num
print(mul_result)