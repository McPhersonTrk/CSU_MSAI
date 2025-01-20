# We are going to find Magic Numbers! Magic numbers are numbers that are both prime and palindrome.
# A prime number is a number that is only divisible by 1 and itself.
# A palindrome is a number that reads the same forwards and backwards.
# Check if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Check if a number is a palindrome.
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Find the magic numbers that are both prime and palindrome.
def find_magic_numbers(limit):
    magic_numbers = []
    for num in range(0, limit):
        if is_prime(num) and is_palindrome(num):
            magic_numbers.append(num)
    return magic_numbers

# Set the limit for finding magic numbers.
try:
    limit = int(input("Enter the limit: "))  # Convert input to integer properly
    magic_numbers = find_magic_numbers(limit)
    print(f'Magic numbers are: {magic_numbers}')
except ValueError:
    print("Please enter a valid integer.")
