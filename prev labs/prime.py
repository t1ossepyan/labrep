import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Введите числа: ").split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Прайм числа:", prime_numbers)
