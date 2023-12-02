import re

def retrieve_numbers_from_text(text):
    return re.findall(r'\d', text)

def combine_first_and_last(elements):
    return elements[0] + elements[-1] if elements else ''

def sum_of_calibration_document(input):
    return sum(
        int(combine_first_and_last(retrieve_numbers_from_text(line)))
        for line in input.splitlines())
