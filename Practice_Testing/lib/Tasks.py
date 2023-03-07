def todo_tasks(tasks):
    _list = []
    for i in tasks:
        if i[:5] == 'TODO:':
            _list.append(i)
    if _list == []:
        return 'No tasks to complete.'
    return _list