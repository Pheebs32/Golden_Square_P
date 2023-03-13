class ReadableEntryFinder():
    def __init__(self, diary):
        self._diary = diary

    def extract(self, wpm, time):
        readable_entries = self.find_readable_entries(wpm, time)
        if len(readable_entries) == 0:
            return None
        return max(readable_entries, key=lambda entry: self._word_count(entry.contents))
    def find_readable_entries(self, wpm, time):
        return [
            entry for entry in self._diary.all()
            if self._entry_readable_in_time(wpm, time, entry)
        ]
    def _entry_readable_in_time(self, wpm, time, entry):
        length_readable = wpm * time
        return self._word_count(entry.contents) <= length_readable
    def _word_count(self, string):
        return len(string.split(" "))
    