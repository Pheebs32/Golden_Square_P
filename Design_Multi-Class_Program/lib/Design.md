
# User Stories
>As a user
>So that I can record my experiences
>I want to keep a regular diary

>As a user
>So that I can reflect on my experiences
>I want to read my past diary entries

>As a user
>So that I can reflect on my experiences in my busy day
>I want to select diary entries to read based on how much time I have and my reading speed

>As a user
>So that I can keep track of my tasks
>I want to keep a todo list along with my diary
* Add todos, completed, incompleted and lists

>As a user
>So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary entries

<!-- Phone numbers start with a zero and are 11 digits long -->
# All variables
* Diary
* Diary entries
* Experiences
* Time
* Reading Speed
* Todo List
* Tasks
* Phone Numbers
* List of numbers
# Counter-parts
* Records
* Keep
* Reflect 
* Read
* Select
* See a list
* Mark Complete
* List Complete
* List incomplete
* Add
# Diagram
Diary_Entry < = > Diary < = > Phone_Number_Exatractor
Diary < = > Readable_Entry_Finder
TaskList < = > Task
# Boiler Code
```python
class Diary():
    def add(self, diary_entry):
        # diary_entry: instance of DiaryEntry
        # returns: nothing
        # side-effects: adds to a list of diary entries
        pass

    def all(self):
        # returns an list of DiaryEntry instances
        pass

class DiaryEntry():
    # public properties: 
    # title: a string representing the title
    # contents: a string repressenting the contents
    def __init__(self, title, contents):
        # title: a string repressenting the title
        # contents: a string repressenting the contents
        # side_effects: sets the above properties
        pass

class TaskList():
    def add(self, task):
        # task: an instance of Task
        # returns: nothing
        # side_effects: add to list of tasks
        pass

    def all_incomplete(self):
        # returns: a list of instances of Task
        #   representing the incomplete tasks
        pass

    def all_complete(self):
        # returns a list of instances of Task
        #   representing the complete tasks
        pass

class Task():
    # public properties:
    # title: a string representing a job to do
    def __init__(self, title):
        # title: a string representing a job to do
        # side_effects: sets the above properties
        pass

    def mark_complete(self):
        # side_effects: marks the task as complete
        # returns: nothing

class PhoneNumberExtractor():
    def __init__(self, diary):
        # diary: an instance of Diary
        # side_effects: set the above properties
        pass

    def extract(self):
        # returns: a list of strings representing
        #   a list of phone numbers
        pass

class ReadableEntryFinder():
    def __init__(self, diary):
        # diary: an instance of Diary
        # side_effects: set the above properties
        pass

    def extract(self, wpm, time):
        # wpm: integer
        # time: interger
        # returns: the longest diary entry that can be read
        #   in the time given, the wpm and time
        pass
```
# Create example intergration tests
```python
'''When I add multiple diary entries
all() lists them out in the order the where added'''

diary = Diary()
entry_1 = DiaryEntry("my title 1", "My contents 1")
entry_2 = DiaryEntry("my title 2", "My contents 2")
entry_3 = DiaryEntry("my title 3", "My contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() # => (entry_1, entry_2, entry_3)

'''When multiple tasks are added
and one is marked complete
all_incomplete() only lists the incomplete tasks'''

task_list = TaskList()
task_1 = Task("Hoover")
task_2 = Task("Hoover")
task_3 = Task("Hoover")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_1.mark_complete()
task_list.all_incomplete() # => [task_2, task_3]


'''When multiple tasks are added
and one is marked complete
all_complete() only lists the complete tasks'''

task_list = TaskList()
task_1 = Task("Hoover")
task_2 = Task("Hoover")
task_3 = Task("Hoover")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_1.mark_complete()
task_list.all_complete() # => [task_1]


'''When multiple diary entries are added
and PhoneNumberExtract() is called
duplicate numbers are ignored'''

diary = Diary()
entry_1 = DiaryEntry("My title 1", "Phone Number 07000000000 and 07000000000")
entry_2 = DiaryEntry("My title 2", "Phone Number 07000000000")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["07000000000"]

'''When multiple diary entries are added
and PhoneNumberExtractor() is called
non-valid numbers are ignored'''

diary = Diary()
entry_1 = DiaryEntry("My title 1", "Phone Number 07000000000 and 07000000000 and 0763 45156")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

'''When no diary entries are added
and PhoneNumberExtractor() is called
it returns an empty list'''

diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

'''When no diary entries are added
and ReadableEntryExtraction() is called
with a wpm of 2 and time of 2
it returns none'''

diary = Diary()
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm = 2, time = 2) # => None

'''When a diary entry that fits in the time
and ReadableEntryExtraction() is called
with a wpm of 2 and time of 2
it returns that diary entry'''

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm = 2, time = 2) # => entry_1

'''When a diary entry that does not fit in the time
and ReadableEntryExtraction() is called
with a wpm of 2 and time of 2
it returns none'''

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm = 2, time = 2) # => None

'''When multiple diary entries are added, one being readable
and ReadableEntryExtraction() is called
with a wpm of 2 and time of 2
it returns the readable entry'''

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm = 2, time = 2) # => entry_2


'''When multiple diary entries are added, several being readable
and ReadableEntryExtraction() is called
with a wpm of 2 and time of 2
it returns the longest readable entry'''

diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
entry_2 = DiaryEntry("Title", "one two three")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm = 2, time = 2) # => entry_2




```
# Create examples of unit tests
```python
# Diary
'''
Initially, Diary has no enteries
'''
diary = Diary()
diary.all() # => []

# DiaryEntry
'''
DiaryEntery is formated with a title and contents
'''
entry = DiaryEntry("My title", "My contents")
entry.title # => "My title"
entry.contents # => "My contents"

# TaskList
'''
Inititally, TaskList has no tasks
'''
task_list = TaskList()
task_list.add() # => []

# TaskList
'''
Initially, TaskList has no complete tasks
'''
task_list = TaskList()
task_list.all_complete # => []
# Task
'''
Task is formated with a title
'''
task = Task("Hoover")
task.title # => "Hoover"
```