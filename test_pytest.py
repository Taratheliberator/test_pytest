
import pytest

def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("test_input", [-100, -1, 0, 1, 100])
def test_even_numbers(test_input):
    if test_input % 2 == 0:
        assert is_even(test_input)
    else:
        assert not is_even(test_input)

@pytest.mark.parametrize("test_input", [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_odd_numbers(test_input):
    if test_input % 2 != 0:
        assert is_even(test_input) == False

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0

if __name__ == '__main__':
    pytest.main()
