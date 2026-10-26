import re

with open("mobile_numbers.txt", "r") as file:
    text = file.read()

numbers = re.findall(r'(?<!\d)[6-9]\d{9}(?!\d)', text)

print("Valid Indian Mobile Numbers:")
for number in numbers:
    print(number)