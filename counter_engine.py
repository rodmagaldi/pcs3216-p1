from helper.decoder import decode_special_character, decode_regular_character
from helper.lower import to_lower_regular_character, to_lower_special_character
from helper.identifier import is_letter_or_number, is_space_or_linebreak, is_punctuation


class CounterEngine:

    def __init__(self, input_text, keywords):
        self.input_text = input_text
        self.keywords = keywords
        self.input_text_size = len(input_text)
        self.words_count = {}
        self.current_word = ""

    def run(self):
        iterator = 0

        while iterator < self.input_text_size:
            character = self.input_text[iterator]

            try:
                character = to_lower_regular_character(character)
                decoded = decode_regular_character(character)
            except:
                '''
                Se nao couber em 1 byte (caractere especial, em geral letras acentuadas),
                criamos um bytestring, concatenamos o byte seguinte e então fazemos
                o decode dele
                '''
                iterator += 1
                next_character = self.input_text[iterator]
                next_character = to_lower_special_character(next_character)

                decoded = decode_special_character(character, next_character)
            finally:
                self.execute_main_loop(decoded)
                iterator += 1
                self.compute_last_word(iterator)

    def execute_main_loop(self, character):
        if (is_letter_or_number(character)):
            self.update_current_word(character)

        elif (is_space_or_linebreak(character)):
            is_valid_word = self.is_current_word_valid()

            if (is_valid_word):
                self.compute_current_word()
                self.empty_current_word()

        elif (is_punctuation(character)):
            is_valid_word = self.is_current_word_valid()

            if (is_valid_word):
                self.compute_current_word()
                self.empty_current_word()

            self.update_current_word(character)
            self.compute_current_word()
            self.empty_current_word()

        else:
            pass

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
