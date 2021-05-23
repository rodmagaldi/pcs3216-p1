from helper.const import special_vowels_array, special_char_dict


class OrdererEngine:

    def __init__(self, unordered_dict):
        self.unordered_dict = unordered_dict
        self.unordered_dict_size = len(unordered_dict)
        self.unordered_list = list(unordered_dict.keys())
        self.ordered_list = []
        self.ordered_dict = {}

    def run(self):
        for current_word in self.unordered_list:

            if len(self.ordered_list) == 0:
                self.ordered_list.append(current_word)

            else:
                for comparing_word in self.ordered_list:

                    if (self.is_current_smaller_than_comparing(current_word, comparing_word)):
                        self.ordered_list.insert(
                            self.ordered_list.index(comparing_word), current_word)
                        break

                    if (self.ordered_list.index(comparing_word) == len(self.ordered_list) - 1):
                        self.ordered_list.append(current_word)
                        break

        self.generate_ordered_dict()

    def is_current_smaller_than_comparing(self, current_word, comparing_word):

        number_of_letters = min(len(current_word), len(comparing_word))

        iterator = 0
        while iterator < number_of_letters:

            current_letter = current_word[iterator]
            comparing_letter = comparing_word[iterator]

            if(current_letter in special_vowels_array):
                for regular_char, special_chars_list in special_char_dict.items():
                    if (current_letter in special_chars_list):
                        current_letter = regular_char

            if(comparing_letter in special_vowels_array):
                for regular_char, special_chars_list in special_char_dict.items():
                    if (comparing_letter in special_chars_list):
                        comparing_letter = regular_char

            if(current_letter > comparing_letter):
                return False
            if(comparing_letter > current_letter):
                return True

            iterator += 1

        if (len(current_word) > number_of_letters):
            return False
        return True

    def generate_ordered_dict(self):
        for word in self.ordered_list:
            self.ordered_dict[word] = self.unordered_dict[word]
