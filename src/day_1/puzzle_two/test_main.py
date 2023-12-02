from main import (
    sum_of_calibration_document,
    retrieve_numbers_from_text,
    combine_first_and_last,
    convert_spelled_out_number_to_digit)

def test_convert_spelled_out_number_to_digit():
    assert convert_spelled_out_number_to_digit('one') == '1'
    assert convert_spelled_out_number_to_digit('two') == '2'
    assert convert_spelled_out_number_to_digit('three') == '3'
    assert convert_spelled_out_number_to_digit('four') == '4'
    assert convert_spelled_out_number_to_digit('five') == '5'
    assert convert_spelled_out_number_to_digit('six') == '6'
    assert convert_spelled_out_number_to_digit('seven') == '7'
    assert convert_spelled_out_number_to_digit('eight') == '8'
    assert convert_spelled_out_number_to_digit('nine') == '9'
    assert convert_spelled_out_number_to_digit('1') == '1'
    assert convert_spelled_out_number_to_digit('2') == '2'
    assert convert_spelled_out_number_to_digit('3') == '3'
    assert convert_spelled_out_number_to_digit('4') == '4'
    assert convert_spelled_out_number_to_digit('5') == '5'
    assert convert_spelled_out_number_to_digit('6') == '6'
    assert convert_spelled_out_number_to_digit('7') == '7'
    assert convert_spelled_out_number_to_digit('8') == '8'
    assert convert_spelled_out_number_to_digit('9') == '9'

def test_combine_first_and_last():
   assert combine_first_and_last(['1', '2']) == '12'
   assert combine_first_and_last(['3', '8']) == '38'
   assert combine_first_and_last(['1', '2', '3', '4', '5']) == '15'
   assert combine_first_and_last(['7']) == '77'
   assert combine_first_and_last([]) == ''

def test_retrieve_numbers_from_text():
    assert retrieve_numbers_from_text('two1nine') == ['2', '1', '9']
    assert retrieve_numbers_from_text('eightwothree') == ['8', '2', '3']
    assert retrieve_numbers_from_text('abcone2threexyz') == ['1', '2', '3']
    assert retrieve_numbers_from_text('xtwone3four') == ['2', '1', '3', '4']
    assert retrieve_numbers_from_text('4nineeightseven2') == ['4', '9', '8', '7', '2']
    assert retrieve_numbers_from_text('zoneight234') == ['1', '8', '2', '3', '4']
    assert retrieve_numbers_from_text('7pqrstsixteen') == ['7', '6']

def test_sum_of_calibration_document():
    input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

    assert sum_of_calibration_document(input) == 281

def test_sum_of_calibration_puzzle_input():
    input = ''
    with open('calibration.txt', 'r') as file:
        input = file.read()

    assert sum_of_calibration_document(input) == 56017
