
## User Story
> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## Solicited Requirements
 - A Function
 - Input: String of Words -> A piece of text
 - Output: A float -> Length of time in minutes to read the text

##Map of Desired Behaviour
1. My function will take as a parameter a string of words.
1. My function will output as a `int` the length of time in minutes that it should take to read the text.
1. The returned `int` will be calculated at an average reading speed of 200wpm.


##Failing Unit Test
Boiler Plate Code:
```python
def reading_time(text: str):
    return 0
```

Unit Test Framework:
```python
from lib.Reading_Time import *

def test_reading_time_generic():
    # make some assertions
    pass

def test_reading_time_empty_text():
    # make some assertions
    pass

def test_very_short_text():
    # make some assertions
    pass

def test_very_long_text():
    # make some assertions
    pass
```

##Pad out your tests!
First, build out your tests.
Yes, they are supposed to fail, but not at runtime, *only* on assertions
```python
from lib.Reading_Time import *

def test_reading_time_generic():
    assert reading_time("sample text "*640) == 4

def test_reading_time_empty_text():
    assert reading_time("") == 0

def test_very_short_text():
    assert reading_time("No") == 1

def test_very_long_text():
    assert reading_time("word "*20000) == 100
```

##Passing Implementation
Now, work on making all of your tests pass.
```python
def reading_time(text: str):
    return 0.0
```
