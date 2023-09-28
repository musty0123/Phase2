# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: none

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        


    def list(self):
        # Returns:
        #   a list of tasks that needs to do
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No lists

 # EXAMPLE

"""
Given nothing, the list returns ==> []
"""
tasks = Task_Tracker()

tasks.list() ==> []

"""
Given a task
returns said task

"""
tasks = Task_Tracker()
tasks.add('task 1')
tasks.list() ==> ['task 1']

"""
Given a list of tasks
returns the list
"""
tasks = Task_Tracker()
tasks.add('task 1')
tasks.add('task 3')
tasks.add('task 2')
tasks.list() ==> ['task 1']  