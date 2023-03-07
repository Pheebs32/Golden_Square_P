from lib.Tasks import *

def test_all_tasks():
    tasks = ['TODO: Hoover', 'TODO: Washing']
    assert todo_tasks(tasks) == tasks

def test_some_tasks():
    tasks = ['TODO: Hoover', 'Washing']
    assert todo_tasks(tasks) == [tasks[0]]

def test_no_tasks():
    tasks = ['Hoover', 'Washing']
    assert todo_tasks(tasks) == 'No tasks to complete.'