from Todo import Todo
class TodoList:
    def __init__(self):
        self._list = []

    def add(self, todo: Todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        output = []
        for i in self._list:
            if i.complete == False:
                output.append(i)
        return output

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        output = []
        for i in self._list:
            if i.complete == True:
                output.append(i)
        return output

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self._list:
            i.complete = True