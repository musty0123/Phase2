import pytest
from lib.todo_checker import *

def test_task_to_do():
    result = extract_tasks("There is something you have #TODO")
    assert result == "task: There is something you have"
    result1 = extract_tasks("There is #TODO something you have")
    assert result1 == "task: There is something you have"
    result2 = extract_tasks("#TODO There is something you have")
    assert result2 == "task: There is something you have"

def test_not_task():
    result = extract_tasks("There is something you have")
    assert result == "No #TODO found"

def test_empty_task():
    with pytest.raises(Exception) as e:
        extract_tasks("")
    error_message = str(e.value)
    assert error_message == "No task was found"

def test_TODO_nothing():
    result = extract_tasks("#TODO")
    assert result == 'YOU HAVE TO DO SOMETHING'

