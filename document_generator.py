import random


def calculate_validator_digit(list: list, digit_multiplier: int):
    evaluation_number_list = list
    total = []
    multiplier = digit_multiplier
    length = len(evaluation_number_list)
    digit = 0

    for i in range(length):
        multiplier = multiplier - 1
        document_index_number = evaluation_number_list[int(i)]
        result = int(document_index_number) * multiplier
        total.append(result)

    digit_division = sum(total) % 11

    if digit_division < 2:
        return digit
    elif digit_division >= 2:
        digit = 11 - digit_division
        return digit


def generate_random_digits():
    numbers_list = []
    number_of_entries = 9

    for number in range(number_of_entries):
        random_number = random.randint(1, 9)
        numbers_list.append(random_number)

    return numbers_list


def convert_list(list):
    formatted_string = ""
    for number in list:
        formatted_string += str(number)

    return formatted_string


def generate_valid_document():
    numbers_list = generate_random_digits()
    numbers_list.append(calculate_validator_digit(list=numbers_list, digit_multiplier=len(numbers_list) + 1))
    numbers_list.append(calculate_validator_digit(list=numbers_list, digit_multiplier=len(numbers_list) + 1))

    return convert_list(numbers_list)

