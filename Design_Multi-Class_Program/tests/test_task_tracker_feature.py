from lib.Task import *
from lib.Task_List import *


''' When multiple tasks are added
and one is marked complete
all_incomplete() only lists the incomplete tasks'''

def test_adds_and_lists_incomplete_tasks():
    task_list = TaskList()
    task_1 = Task("Hoover")
    task_2 = Task("Hoover")
    task_3 = Task("Hoover")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    task_1.mark_complete()
    assert task_list.all_incomplete() == [task_2, task_3]


'''When multiple tasks are added
and one is marked complete
all_complete() only lists the complete tasks'''

def test_adds_and_lists_complete_tasks():
    task_list = TaskList()
    task_1 = Task("Hoover")
    task_2 = Task("Hoover")
    task_3 = Task("Hoover")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    task_1.mark_complete()
    assert task_list.all_complete() == [task_1]

