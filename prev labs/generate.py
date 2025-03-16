#1

def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")

#2

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_numbers(n))))

#3

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
print(list(divisible_by_3_and_4(n)))

#4

import json

data = {"name": "Alice", "age": 25, "city": "New York"}
json_data = json.dumps(data)  # Convert to JSON string
print(json_data)

python_data = json.loads(json_data)
print(python_data["name"])  # Alice

