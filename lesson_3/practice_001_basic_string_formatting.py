# Given the following variables:
name = "Emily"
age = 26
job_title = "QA Manager"

# print (name + ' is a ' + str(age) + 'year old ' + job_title + ' of our company')

# For each practice, print the following message using
# the requested string formatting method:
# "Emily is a 26 years old QA manager of our company"
# print ("{name} is a {age} years old {job_title} of our company .".format( name= name,age=age,job_title=job_title))
# Practice 1.1 - Using concatenation with +
# (your solution goes here)

# Practice 1.2 - Using .format()
# (your solution goes here)

# Practice 1.3 - Using f-strings
# (your solution goes here)
message = f"{name} is a {age} years old {job_title} of our company"
print(message)