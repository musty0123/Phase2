# EXAMPLE

def extract_tasks(task):
    """check if string contains #TODO, if so return true

    Parameters: (list all parameters and their types)
        task: a string containing words (e.g. "I have to do #TODO")

    Returns: 'You have to do {task}'
'You have to do {task}'
        a string    """ if true

        'This is not a to do task if false'
    Side effects: (state any side effects)
        No side effects
    pass # Test-driving means _not_ writing any code here yet.

    # EXAMPLE

"""
Given a text that contains #TODO, 
it returns the string
"""
extract_tasks("This is a task you have #TODO") => ["You have to : This is a task you have"]

"""
Given a text with no #TODO
return a different string

"""
extract_Tasks("This is a task you have ") => 'No #TODO Found'

"""
Given an empty string 
it returns exception error
I
"""
extract_tasks("") => 'No text found'

"""
Given #TODO with no tasks
It returns a string
"""
extract_tasks("#TODO") => 'YOU HAVE TO DO SOMETHING™

"""
