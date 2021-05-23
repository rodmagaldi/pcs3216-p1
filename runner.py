from counter_engine import CounterEngine
from orderer_engine import OrdererEngine


class Runner:
    def __init__(self, input_file_path, keywords):
        self.input_file_path = input_file_path
        self.keywords = keywords
        self.file_content = ""

    def configure_file(self):
        with open(self.input_file_path, 'rb') as text_file:
            self.file_content = text_file.read()

    def configure_keywords(self):
        self.keywords = list(map(lambda item: item.lower(), self.keywords))

    def run(self):
        self.configure_file()
        self.configure_keywords()

        word_counter = CounterEngine(self.file_content, self.keywords)
        word_counter.run()
        unordered_dict = word_counter.words_count

        word_orderer = OrdererEngine(unordered_dict)
        word_orderer.run()
        ordered_dict = word_orderer.ordered_dict

        return ordered_dict
