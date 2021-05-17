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