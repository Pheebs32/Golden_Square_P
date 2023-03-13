class GrammarStats:
    def __init__(self):
        self.correct = False
        self.count = 0
        self.counters = 0
        self.overall = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.overall += 1
        front = text[0]
        end = text[-1]
        punctuation = ['!', '?', '.']
        if (front == front.upper()) and (end in punctuation):
            self.count += 1
            self.correct = True
            print (self.overall)
            grammar.percentage_good()
            return True
        self.counters += 1
        self.correct = False
        print (self.overall)
        grammar.percentage_good()
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        overall_1 = self.overall / 100
        correct_1 = self.count / overall_1
        print(correct_1)
        return correct_1

grammar = GrammarStats()
grammar.check("Hello, this is a sentance.")
grammar.check("this is another sentace")
grammar.check("this is another sentace")
grammar.check("Hello, this is a sentance.")
