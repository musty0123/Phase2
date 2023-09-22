from lib.count_words import *
import pytest


# input = ' a cat with a hat ' output = ' 5 '
def test_a_sentence():
    result = count_words("a cat with a hat")
    assert result == 5
# input = '' output ' there is no string to count '
def test_empty():
    
    with pytest.raises(Exception) as e:
        count_words('')

    error_message = str(e.value)   
    assert error_message == 'No text inserted'
# input = 'animals with hats : cats'
def test_punctutation():
    result = count_words("animals with hats : cats")
    assert result == 4
