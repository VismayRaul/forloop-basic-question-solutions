#----------------------------------------PALINDROME---------------------------------------------
palindrome = input('Enter any number')
reversed_palindrome = palindrome[::-1]
if palindrome==reversed_palindrome:
    print(palindrome,'is a palindrome')
else:
    print(palindrome,'is not a palindrome')