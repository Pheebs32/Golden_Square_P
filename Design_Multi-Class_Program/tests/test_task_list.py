from lib.Task_List import *

''' Inititally, TaskList has no incomplete tasks '''
def test_task_incomplete_is_empty():
    task_list = TaskList()
    assert task_list.all_incomplete() == []

''' Inititally, TaskList has no complete tasks '''
def test_task_incomplete_is_empty():
    task_list = TaskList()
    assert task_list.all_complete() == []
