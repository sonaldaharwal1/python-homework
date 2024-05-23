# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.

def is_palindrome(word):

    word = word.lower()

  reversed_word = word[::-1]

  if


word = input("Enter a word: ")
print(is_palindrome(word))