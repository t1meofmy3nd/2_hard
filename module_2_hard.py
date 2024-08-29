from random import randint


def get_number():
    number = randint(3, 20) # Определя
    return number
def get_pairs_for_first(number, first):
    result = ""
    for second in range(first + 1, number):
        if number % (first + second) == 0:
            result += str(first) + str(second)
    return result
def get_result(number):
    result = ""
    for first in range(1, number):
        result += get_pairs_for_first(number, first)
    return result

def main():
    number = get_number()
    result = get_result(number)
    print(f"{number} - {result}")


main()
