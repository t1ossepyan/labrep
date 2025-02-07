import random
import itertools
import math

# 1. Функция для перевода граммов в унции
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2. Функция для перевода градусов Фаренгейта в Цельсии
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# 3. Функция для нахождения количества куриц и кроликов
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits
    return "Нет решений"

# 4. Функция для фильтрации простых чисел
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 5. Функция для вывода всех перестановок строки
def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# 6. Функция для переворачивания слов в предложении
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# 7. Функция для проверки наличия двух троек подряд
def has_33(nums):
    return any(nums[i] == nums[i + 1] == 3 for i in range(len(nums) - 1))

# 8. Функция для проверки наличия последовательности 0,0,7
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9. Функция для вычисления объема сферы
def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

# 10. Функция для возврата списка уникальных элементов
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 11. Функция для проверки, является ли строка палиндромом
def is_palindrome(s):
    if s[::-1] == s:
        return True

def histrogram(a):
    for i in a:
        print("*"*i)


def Guess_the_number():
    print("""Hello! What is your name?""")
    name = input()
    number = random.randint(1, 20)
    print("Well, ", name , "I am thinking of a number between 1 and 20. \n Take a guess.")
    guesscount = 0
    while True:
        inp = int(input())
        if inp < number:
            print("Your guess is too low. \n Take a guess.")
            guesscount += 1
        if inp > number:
            print("Your guess is too high. \n Take a guess.")
            guesscount += 1
        if inp == number:
            print("Good job,", name, " You guessed my number in", guesscount , "guesses!")
            break





