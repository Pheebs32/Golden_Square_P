class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title} : {self.contents}"

    def count_words(self):
        new_str = self.contents.strip()
        in_word = 0
        count = 0
        for i in new_str:
            if i != " ":
                if in_word == 0:
                    count += 1
                    in_word = 1
            else:
                if in_word == 1:
                    in_word = 0
        return count

    def reading_time(self, wpm):
        return (self.count_words() / wpm)