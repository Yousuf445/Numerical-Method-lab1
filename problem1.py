
numbers = [5, 8, 3, 9, 1, 7]

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
