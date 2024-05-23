# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678

def reverse_integer(num):
reversed_str = str(num)[::-1]

    # Check if the number was negative
    if num < 0:
        # If negative, remove the '-' sign from the reversed string
       print( reversed_str = '-' + reversed_str[:-1]

    else:
        print(int(reversed_str))

num = -876
reversed_num = reverse_integer(num)
print("Reversed integer:", reversed_num)