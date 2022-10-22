from math import *

digits = []
is_palindrome = True

num = input("Input your number: ")

for digit in num:
    digits.append(str(digit))

print(digits)

for i in range(round(len(digits)/2)):
    if digits[i] != digits[-(i+1)]:
        is_palindrome = False

if is_palindrome:
    print("Your number is palindrome!")
else:
    print("Your number is not palindrome!")