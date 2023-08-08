def collatz_conjecture(n):
    nums = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        nums.append(n)
    return nums

# Prompt the user to enter a starting number
n = int(input("Please enter a starting number: "))

# Call the collatz_conjecture function to perform the calculation
numbers = collatz_conjecture(n)

# Print the result
print(f"Starting number: {n}, Numbers: {numbers}")