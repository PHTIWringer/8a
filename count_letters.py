# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 05/15/2024
# Description: Program that a string as a parameter and returns a dictionary that tabulates how many of each letter is in that string.

def count_letters(input_string):
    '''Function that takes in a string and returns each letter and the a count of how many are shared'''
    letter_counts = {}

    for char in input_string:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            upper_char = char.upper()
            if upper_char in letter_counts:
                letter_counts[upper_char] += 1
            else:
                letter_counts[upper_char] = 1
    return letter_counts

# print(count_letters("AaBb"))
