from lib.Todo import *
'''
string - representing a task
task == task
Complete === Boolean
'''
def test_todo_init():
    task = Todo("todo: washing")
    assert task.task == "todo: washing"
    assert task.complete == False

'''

'''
def test_mark_complete():
    task = Todo("")
    task.mark_complete()
    assert task.complete == True