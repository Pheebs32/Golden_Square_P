from lib.Task import *

''' Task is formated with a title '''
def test_task_format():
    task = Task("Hoover")
    assert task.title == "Hoover"


'''  Test newly formatted tasks are not complete '''
def test_task_format_incomplete():
    task = Task("Hoover")
    assert task.complete == False

''' When a test is marked complete
It is returnd in the complete property '''
def test_marks_tasks_complete():
    task = Task("Hoover")
    task.mark_complete()
    assert task.complete == True