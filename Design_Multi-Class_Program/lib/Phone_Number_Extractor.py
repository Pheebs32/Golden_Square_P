import re

class PhoneNumberExtractor():
    def __init__(self, diary):
        self.diary = diary

    def extract(self):
        phone_numbers = set()
        for entry in self.diary.all():
            extracted = re.findall(r"\b0[0-9]{10}\b", entry.contents)
            phone_numbers.update(extracted)
        return phone_numbers
