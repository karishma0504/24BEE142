# Prompt: Check whether a given number is prime, perfect, Armstrong, palindrome, and automorphic

num = int(input("Enter a number: "))

# Prime
prime = True
if num < 2:
    prime = False
for i in range(2, num):
    if num % i == 0:
        prime = False
        break

# Perfect
perfect = False
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
if sum_factors == num:
    perfect = True

# Armstrong
temp = num
sum_cubes = 0
while temp > 0:
    d = temp % 10
    sum_cubes += d*d*d
    temp = temp // 10
armstrong = (sum_cubes == num)

# Palindrome
palindrome = (str(num) == str(num)[::-1])

# Automorphic
automorphic = (str(num*num).endswith(str(num)))

# Results
print("Prime:", prime)
print("Perfect:", perfect)
print("Armstrong:", armstrong)
print("Palindrome:", palindrome)
print("Automorphic:", automorphic)
