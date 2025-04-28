# Prompt: If a positive integer is entered through the keyword,
# write a recursive function to obtain the prime factors of the number.

# Define the recursive function
def prime_factors(n, i=2):
    # Base case: If n becomes 1, return an empty list
    if n == 1:
        return []

    # If i divides n, it's a prime factor, then recurse with reduced n
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    else:
        # Otherwise, move to the next number
        return prime_factors(n, i + 1)


# Example usage
num = int(input("Enter a positive integer: "))
factors = prime_factors(num)
print(f"Prime factors of {num}: {factors}")
