import re

def convert_spelled_out_number_to_digit(text_number):
    conversion_table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return conversion_table[text_number] if text_number in conversion_table else text_number

def retrieve_numbers_from_text(text):
    return [
        convert_spelled_out_number_to_digit(number)
        for number in re.findall(
                r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',
                text)
    ]

def combine_first_and_last(elements):
    return elements[0] + elements[-1] if elements else ''

def sum_of_calibration_document(input):
    return sum(
        int(combine_first_and_last(retrieve_numbers_from_text(line)))
        for line in input.splitlines())
