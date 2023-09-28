from lib.GrammarStats import *

def test_check():
    text = GrammarStats()
    result = text.check('This sentence stsrts with a capital.')
    assert result == True
    result2 = text.check('this sentence does not start with a capital letter.')
    assert result2 == False
    result3 = text.check('This sentence does not end with punctuation')
    assert result3 == False

def test_percentage():
    text = GrammarStats()
    text.check('This sentence does not end with punctuation')
    text.check('this sentence does not start with a capital letter.')
    text.check('This sentence stsrts with a capital.')
    text.check('This senten stsrts with a capital.')
    result = text.percentage_good()
    assert result == 50
