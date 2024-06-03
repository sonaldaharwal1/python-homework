steps = []
#
# # Ask the user for the number of steps taken each day of the week
# monday = int(input('Steps for Monday: '))
# tuesday = int(input('Steps for Tuesday: '))
# wednesday = int(input('Steps for Wednesday: '))
# thursday = int(input('Steps for Thursday: '))
# friday = int(input('Steps for Friday: '))
# saturday = int(input('Steps for Saturday: '))
# sunday = int(input('Steps for Sunday: '))
#
# # Append the steps for each day to the list
# steps.append([monday, tuesday, wednesday, thursday, friday, saturday, sunday])
#
# # Steps on Wednesday
# print("Steps on Wednesday:", steps[2])
#
# # Steps on the work days (Mon - Fri)
# work_days_steps = steps[0:5]
# print("Steps on work days (Mon - Fri):", sum(work_days_steps))
#
# # Total steps over the whole week
# print("Total steps over the whole week:", sum(steps))
#
# # Least number of steps
# print("Least number of steps:", min(steps))
#
# # Highest number of steps
# print("Highest number of steps:", max(steps))
# user_input =input('input any phrase')
#
# # Split user input into words
# words = user_input.split()
# print(words)
#
# # Reverse the list and print it
# reversed_words =list (reversed(words))
# print(reversed_words)
#
# # Print the length of the words list
# print(len(words))
numbers = [5, 2, 9, 1, 5, 6]
    # Sort the list of numbers
numbers=numbers.sort()
print(numbers)
    # Initialize the two lowest numbers as the first two elements of the sorted list
lowest_1 = numbers[0]
lowest_2 = numbers[1]

    # Iterate through the sorted list starting from the third element
for num in numbers[2:]:
        # If the current number is smaller than lowest_1
        if num < lowest_1:
            # Shift the previous lowest_1 to lowest_2 and update lowest_1
            lowest_2 = lowest_1
            lowest_1 = num
        # If the current number is smaller than lowest_2
        elif num < lowest_2:
            # Update lowest_2
            lowest_2 = num

else:
    print(lowest_1, lowest_2)