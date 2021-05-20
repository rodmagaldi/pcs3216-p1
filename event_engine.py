from functools import cmp_to_key
import locale

from const import BEGIN_CAPITAL_LETTERS, CR, END_CAPITAL_LETTERS, BEGIN_CAPITAL_SPECIAL_LETTERS, END_CAPITAL_SPECIAL_LETTERS, BEGIN_LOWER_CASE_LETTERS, END_LOWER_CASE_LETTERS, BEGIN_LOWER_CASE_SPECIAL_LETTERS, END_LOWER_CASE_SPECIAL_LETTERS, BEGIN_NUMBERS, END_NUMBERS, LF, SPACE

locale.setlocale(locale.LC_ALL, 'pt_BR')


class EventEngine:

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

            try:
                character = self.to_lower_regular_character(character)
                decoded = bytes([character]).decode('utf-8')
            except:
                '''
                Se nao couber em 1 byte (caractere especial, em geral letras acentuadas),
                criamos um bytestring, concatenamos o byte seguinte e então fazemos
                o decode dele
                '''
                iterator += 1
                char_array = bytearray(bytes([character]))

                next_character = self.input_text[iterator]
                next_character = self.to_lower_special_character(
                    next_character)
                new_char_array = bytearray(bytes([next_character]))

                array = char_array + new_char_array
                decoded = array.decode('utf-8')
            finally:
                self.execute_main_loop(decoded)
                iterator += 1
                self.compute_last_word(iterator)

    def to_lower_regular_character(self, character):
        if (BEGIN_CAPITAL_LETTERS <= character <= END_CAPITAL_LETTERS):
            return character + 32
        return character

    def to_lower_special_character(self, character):
        if (BEGIN_CAPITAL_SPECIAL_LETTERS <= character <= END_CAPITAL_SPECIAL_LETTERS):
            return character + 32
        return character

    def execute_main_loop(self, character):
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

    def generate_results(self):
        ordered_keys = sorted(self.words_count.keys(),
                              key=cmp_to_key(locale.strcoll))
        for (key) in ordered_keys:
            self.ordered_count[key] = self.words_count[key]
        return self.ordered_count

    def is_letter_or_number(self, character):
        byte_list = list(character.encode('utf-8'))
        new_char = byte_list[-1]
        return (BEGIN_NUMBERS <= new_char <= END_NUMBERS) or (BEGIN_CAPITAL_LETTERS <= new_char <= END_CAPITAL_LETTERS) or (BEGIN_LOWER_CASE_LETTERS <= new_char <= END_LOWER_CASE_LETTERS) or (BEGIN_LOWER_CASE_SPECIAL_LETTERS <= new_char <= END_LOWER_CASE_SPECIAL_LETTERS) or (BEGIN_CAPITAL_SPECIAL_LETTERS <= new_char <= END_CAPITAL_SPECIAL_LETTERS)

    def is_space_or_linebreak(self, character):
        byte_list = list(character.encode('utf-8'))
        return byte_list[-1] in [CR, LF, SPACE]

    def is_punctuation(self, character):
        return (not self.is_letter_or_number(character) and not self.is_space_or_linebreak(character))

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
