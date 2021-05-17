from event_engine import EventEngine

class Runner:
    def __init__(self, input_file_path, keywords):
        self.input_file_path = input_file_path
        self.keywords = keywords
        self.file_content = ""
    
    def configure_file(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as text_file:
            self.file_content = text_file.read().lower()
        
    def configure_keywords(self):
        self.keywords = list(map(lambda item: item.lower(), self.keywords))
        
    def run(self):
        self.configure_file()
        self.configure_keywords()
        
        word_counter = EventEngine(self.file_content.lower(), self.keywords)
        word_counter.run()
        
        return word_counter.generate_results()