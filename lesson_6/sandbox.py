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
user_input =input('input any phrase')

# Split user input into words
words = user_input.split()
print(words)

# Reverse the list and print it
reversed_words =list (reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))
