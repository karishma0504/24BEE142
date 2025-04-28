# Prompt: Print nCr (Combination) and nPr (Permutation)

import math

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# nCr (Combination) = n! / (r! * (n - r)!)
nCr = math.comb(n, r)

# nPr (Permutation) = n! / (n - r)!
nPr = math.perm(n, r)

print(f"nCr: {nCr}")
print(f"nPr: {nPr}")
