from lib.reminder import *

class TestReminder():
    def test__init__(self):
        subject = Reminder('Becky')
        assert subject.name == 'Becky'
    def test_remind_me_to(self):
        subject = Reminder('Becky')
        subject.remind_me_to('Feed dog')
        assert subject.task == 'Feed dog'
        assert subject.remind() ==  f"Feed dog, Becky!"

# from lib.reminder import *

# def test_reminds_the_user_to_do_a_task():
#     reminder = Reminder("Kay")
#     reminder.remind_me_to("Walk the dog")
#     result = reminder.remind()
#     assert result == "Walk the dog, Kay!"
