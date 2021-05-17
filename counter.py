import re
from string import punctuation
from functools import cmp_to_key
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

class EventEngine:
    regex_compiler_letters = re.compile('[A-Za-z0-9À-ÿ]')
    regex_compiler_blank = re.compile('[\n\r\s]')
    
    def __init__(self, input_text, keywords):
        self.input_text = input_text
        self.keywords = keywords
        self.input_text_size = len(input_text)
        self.words_count = {}
        self.current_word = ""
        self.ordered_count = {}
    
    def run(self):
        iterator = 0
        
        while iterator < self.input_text_size:
            character = self.input_text[iterator]
            
            if (self.is_letter_or_number(character)):
                self.update_current_word(character)
            
            elif (self.is_space_or_linebreak(character)):
                is_valid_word = self.is_current_word_valid()
                
                if (is_valid_word):
                    self.compute_current_word()
                    self.empty_current_word()
            
            elif (self.is_punctuation(character)):
                is_valid_word = self.is_current_word_valid()
                
                if(is_valid_word):
                    self.compute_current_word()
                    self.empty_current_word()
                
                self.update_current_word(character)
                self.compute_current_word()
                self.empty_current_word()
                
            else:
                pass
            
            iterator += 1
            
            self.compute_last_word(iterator)
            
    def generate_results(self):
        ordered_keys = sorted(self.words_count.keys(), key=cmp_to_key(locale.strcoll))
        for (key) in ordered_keys:
            self.ordered_count[key] = self.words_count[key]
        return self.ordered_count
    
    def is_letter_or_number(self, character):
        match = EventEngine.regex_compiler_letters.match(character)
        if match:
            return match.group()
        else:
            return None
    
    def is_space_or_linebreak(self, character):
        match = EventEngine.regex_compiler_blank.match(character)
        if match:
            return match.group()
        else:
            return None
    
    def is_punctuation(self, character):
        return character in punctuation
    
    def is_current_word_valid(self):
        return self.current_word != ""
    
    def update_current_word(self, character):
        self.current_word += character
    
    def compute_current_word(self):
        word = self.current_word
        words_count = self.words_count
        
        if (word not in words_count.keys()):
            inner_dict = {}
            words_count[word] = inner_dict
            inner_dict['count'] = 1
        
            if (word in self.keywords):
                inner_dict['keyword'] = True
            
            else:
                inner_dict['keyword'] = False
        
        else:
            words_count[word]['count'] += 1
            
    def empty_current_word(self):
        self.current_word = ""
        
    def compute_last_word(self, iterator):
        if (iterator == self.input_text_size and self.is_current_word_valid()):
            self.compute_current_word()


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


import pandas as pd

class ResultHandler:
    def __init__(self, results_dict, save_path):
        self.results_dict = results_dict
        self.save_path = save_path
        self.results_dataframe = None
        
    def configure_pd(self):
        self.results_dataframe = pd.DataFrame.from_dict(self.results_dict, orient='index')
        pd.set_option('display.max_rows', None)
        
    def save_results(self):
        self.configure_pd()
        self.results_dataframe.to_csv(self.save_path, index=True)

    def show_results(self):
        print(self.results_dataframe)

    def show_keywords_results(self):
        print(self.results_dataframe[self.results_dataframe['keyword'] == True])



keywords_list = ['o', 'Então', 'ali', ',']
runner = Runner('teste.txt', keywords_list)
results = runner.run()
handler = ResultHandler(results, 'teste.csv')
handler.save_results()
handler.show_results()
handler.show_keywords_results()