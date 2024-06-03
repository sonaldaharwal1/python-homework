# name = "Joseph"
#
# for characters in name:
#     print(characters)

#
# name = 'Tom'
# counter = 0
#
# for characters in name:
#     counter += 1
#
# # This should print '3'
# print(counter)

# counter = 0
#
# while counter < 5:
#      counter += 1
#      print(counter)

# counter = 0
#
# while True:
#     counter += 1
#
#     if counter > 5:
#         break
#     print(counter)

# 0, 1, 2, 3, 4, 5 (use only one argument)

# for number in range(6):
#     print(number)

# 0, 1, 2, 3, 4, 5 (use two arguments: start and end)
# for number in range(0,6):
#      print(number)
# #
# # # Odd numbers between 0 and 10: 1, 3, 5, 7, 9
# # for number in range(1,10,2):
# #     print(number)
# for number in range(2,10,2):
#      print(number)

# my_string = 's0m3 str1ng w1th numb3r5'
#
# # Define a string containing all digits
# numbers = '1234567890'
#
# # Flag to keep track if the first digit is found
# first_digit_found = True
#
# # Loop through each character in the string
# for character in my_string:
#     # Check if the character is a digit
#     if character in numbers:
#         # Print the digit
#         print(character)
#
#         # Check if it's the first digit and update the flag
#         if  first_digit_found:
#             first_digit_found = False
#             # If it's the first digit, break the loop to print only the first digit
#             break
# quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
# vowel_count = 0
#
# for charecter in quote:
#     # 'A' and 'a' are different in python, so we include both upper and lowercase
#     #      vowels in our comparison string to account for this difference.
#     if charecter in'aeiouAEIOU':
#         vowel_count += 1
#
# #         print(f"The number of vowels in the quote is: {vowel_count}")
# quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
# vowel_count = 0
#
# # Iterate over each character in the quote
# for char in quote:
#     # Check if the character is a vowel
#     if char in 'aeiouAEIOU':
#         # Increment the vowel count
#         vowel_count += 1
#
# # Print the total number of vowels in the quote
# print(f"The number of vowels in the quote is: {vowel_count}")
#
# quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
# vowel_count = 0
#
# for char in quote:
#     # 'A' and 'a' are different in python, so we include both upper and lowercase
#     # vowels in our comparison string to account for this difference.
#     if char in 'aeiouAEIOU':
#         vowel_count += 1
#
# print(f"The number of vowels in the quote is: {vowel_count}")

# mixed_string = "abc123xyz456"
# digits = "0123456789"
# found_digits = []
#
# for char in mixed_string:
#     if char in digits:
#         found_digits.append(int(char))
#
# print(f"The total sum of numbers in the string is: {sum(found_digits)}")

#


# passwords = ['Passw0rd', 'hello', 'strongPass1', 'weak']
# strong_password_count = 0
#
# for password in passwords:
#     if len(password) >= 8:
#         strong_password_count += 1
#
# print(f"Number of strong passwords: {strong_password_count}")



# colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
# index = 0
#
# # This should basically say: while the current color being evaluated is
# # different than "Red", increment to the next color and try again.
# while colors[index] != "Red":
#     print(f"Found {colors[index]} crayon. Still looking for Red.")
#     index += 1
# # print("Found the Red crayon!")
# numbers = [5, 2, 9, 1, 5, 6]
# # Your code here
# my_sorted_list = sorted(numbers)
# print(my_sorted_list)
# lowest_1 = [0]
# lowest_2 = [1]
#
# # Iterate through the list of numbers
# for num in numbers[2:]:
#         if num < lowest_1:
#             lowest_2 = lowest_1
#             lowest_1 = num
#         elif lowest_1 < num < lowest_2:
#             lowest_2 = num
#         elif num == lowest_1:
#             lowest_2 = lowest_1

# file_name = "My Summer Photos 2023"
# new_file_name = ""
#
# # Loop through each character in the file name
# for char in file_name:
#     # Check if the character is not a space
#     if char != " ":
#         # If it's not a space, add it to the new file name
#         new_file_name += char
#
# # Print the new file name without spaces
# # print("File name without spaces:", new_file_name)
# numbers = [5, 2, 9, 1, 5, 6]
# # # Your code here
# my_sorted_list = sorted(numbers)
# print(my_sorted_list)
# lowest_1= [0]
# lowest_2 =[1]
# for num in numbers[2:]:
#     if num < lowest_1:
#       lowest_2 = lowest_1
#       lowest_1 = num
#   elif lowest_1 < num < lowest_2:
#             lowest_2 = num
#         elif num == lowest_1:
#             lowest_2 = lowest_1


numbers = [5, 2, 9, 1, 5, 6]
my_sorted_list = sorted(numbers)
print(my_sorted_list)

lowest_1 = my_sorted_list[0]  # Initialize lowest_1 with the first element
lowest_2 = my_sorted_list[1]  # Initialize lowest_2 with the second element

for num in my_sorted_list[2:]:
    if num < lowest_1:
        lowest_2 = lowest_1
        lowest_1 = num
    elif lowest_1 < num < lowest_2:
        lowest_2 = num

print("Two lowest elements:", lowest_1, lowest_2)