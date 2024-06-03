# Remove the lowercase vowels in a given string:
# str1 = ‘Hello, World!’
# The vowels are:
# vowels = "aeiou"
# “y” is not considered a vowel for this task. The input string is always in lowercase.
# Examples:
# "hello" --> "hll"
# "goodbye" --> "gdby"
str1 = 'Hello, World!'
vowels = "aeiou"

result = ''
for char in str1:
    if char not in vowels:
        result += char

print(result)