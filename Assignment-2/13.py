# Prompt: Convert number 0 to 19 to its equivalent words. E.g. 0 -> zero, 19 -> nineteen

num = int(input("Enter a number between 0 and 19: "))

words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"
}

if 0 <= num <= 19:
    print(f"The number {num} in words is {words[num]}.")
else:
    print("Please enter a number between 0 and 19.")
