import random

letters = [random.choice('abcdef') for _ in range(20)]
print(letters)

sorted_letters = sorted(letters)
print(sorted_letters)

descending_letters = sorted(letters, reverse=True)
print(descending_letters)

unique_letters = sorted(set(letters))
print(unique_letters)