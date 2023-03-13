from lib.Todo import *
from lib.Todo_List import *

'''
Add tasks to a list with 'TODO'
in the string
'''
def test_add_and_lists_tasks():
    todo = TodoList()
    todo.add(Todo('Washing'))
    todo.add(Todo('Hoover'))
    todo.add(Todo('Washing'))
    todo.add(Todo(' '))
    todo.add(Todo('bjaejoibjkaopj£^@'))
    assert len(todo._list) == 5

'''
Returns a list of all uncompleted 'TODO' tasks
'''
def test_returns_uncompleted_tasks():
    todo = TodoList()
    t = Todo('Washing')
    t.mark_complete()
    todo.add(t)
    t = Todo(' ')
    t.mark_complete()
    todo.add(t)
    todo.add(Todo('Hoover'))
    todo.add(Todo('Washing'))
    todo.add(Todo('bjaejoibjkaopj£^@'))
    incomplete = todo.incomplete()
    assert len(incomplete) == 3
    for i in incomplete:
        assert i.complete == False

'''
Returns a list of all completed 'TODO' tasks
'''
def test_complete():
    todo = TodoList()
    t = Todo('Washing')
    t.mark_complete()
    todo.add(t)
    t = Todo(' ')
    t.mark_complete()
    todo.add(t)
    todo.add(Todo('Hoover'))
    todo.add(Todo('Washing'))
    todo.add(Todo('bjaejoibjkaopj£^@'))
    complete = todo.complete()
    assert len(complete) == 2
    for i in complete:
        assert i.complete == True

'''
Marks all 'TODO' tasks as complete even if not completed
'''
def test_give_up():
    todo = TodoList()
    t = Todo('Washing')
    t.mark_complete()
    todo.add(t)
    t = Todo(' ')
    t.mark_complete()
    todo.add(t)
    todo.add(Todo('Hoover'))
    todo.add(Todo('Washing'))
    todo.add(Todo('bjaejoibjkaopj£^@'))
    todo.give_up()
    assert len(todo.complete()) == 5
