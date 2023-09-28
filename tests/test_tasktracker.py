from lib.tasktracker import *

# Given nothing, the list returns ==> []
def test_empty_list():


    tasks = Task_Tracker()

    result = tasks.list() 
    assert result == []


# Given a task
# returns said task

def test_single_task():
    tasks = Task_Tracker()
    tasks.add('task 1')
    result = tasks.list() 
    assert result == ['task 1']


# Given a list of tasks
# returns the list

def test_set_of_tasks():
    tasks = Task_Tracker()
    tasks.add('task 1')
    tasks.add('task 3')
    tasks.add('task 2')
    result = tasks.list() 
    assert result == ['task 1', 'task 3', 'task 2']  

def test_completed():
    tasks = Task_Tracker()
    tasks.add('task 1')
    tasks.add('task 3')
    tasks.add('task 2')
    tasks.completed('task 3')
    result = tasks.list() 
    assert result == ['task 1', 'task 2']  