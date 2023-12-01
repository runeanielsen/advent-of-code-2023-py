from main import (
    sum_of_calibration_document,
    retrieve_numbers_from_text,
    combine_first_and_last)

def test_combine_first_and_last():
   assert combine_first_and_last(['1', '2']) == '12'
   assert combine_first_and_last(['3', '8']) == '38'
   assert combine_first_and_last(['1', '2', '3', '4', '5']) == '15'
   assert combine_first_and_last(['7']) == '77'
   assert combine_first_and_last([]) == ''

def test_retrieve_numbers_from_text():
    assert retrieve_numbers_from_text('1abc2') == ['1', '2']
    assert retrieve_numbers_from_text('pqr3stu8vwx') == ['3', '8']
    assert retrieve_numbers_from_text('a1b2c3d4e5f') == ['1', '2', '3', '4', '5']
    assert retrieve_numbers_from_text('treb7uchet') == ['7']
    assert retrieve_numbers_from_text('739739') == ['7', '3', '9', '7', '3', '9']

def test_sum_of_calibration_document():
    input = '''1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet'''

    assert sum_of_calibration_document(input) == 142
