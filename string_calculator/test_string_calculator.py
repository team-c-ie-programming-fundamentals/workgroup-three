
from string_calculator import string_calculator

def test_string_calculator_empty_string():
    values = ['', '    ', '                         ']
    for case in values:
        assert string_calculator(case) == 0


def test_string_calculator_zero_with_spaces():
    values = ['    0  ', '0       ', '          0']
    for case in values:
        assert string_calculator(case) == 0


def test_string_calculator_zero_with_numbers():
    values = ['0,2,3,4,5']
    for case in values:
        assert string_calculator(case) == 14
        
def test_string_calculator_not_subsequent_numbers():
    values = ['0,2,7,50,500']
    for case in values:
        assert string_calculator(case) == 559
        

def test_string_calculator_random_spaces_with_numbers():
    values = ['        2,3,4,       5', '2,        3, 4,    5  ']
    for case in values:
        assert string_calculator(case) == 14
        
def test_string_calculator_random_spaces_with_big_numbers():
    values = [' 1 000, 1000', '1 0 0 0, 1 0 0 0']
    for case in values:
        assert string_calculator(case) == 2000        
