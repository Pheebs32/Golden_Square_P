from lib.Todo_List import *

class Todo():
    def __init__(self) -> None:
        self.complete = False

'''
test add function
'''
def test_add():
    task_list = TodoList()
    task_list.add(Todo())
    assert len(task_list._list) == 1

def test_incomplete():
    task_list = TodoList()
    task_list.add(Todo())
    assert len(task_list.incomplete()) == 1

def test_complete():
    task_list = TodoList()
    t = Todo()
    t.complete = True
    task_list.add(t)
    assert len(task_list.complete()) == 1

def test_give_up():
    task_list = TodoList()
    t = Todo()
    t.complete = True
    task_list.add(Todo())
    task_list.add(t)
    task_list.give_up()
    assert len(task_list.complete()) == 2
