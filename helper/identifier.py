from helper.const import (BEGIN_CAPITAL_LETTERS, END_CAPITAL_LETTERS,
                          BEGIN_CAPITAL_SPECIAL_LETTERS, END_CAPITAL_SPECIAL_LETTERS,
                          BEGIN_LOWER_CASE_LETTERS, END_LOWER_CASE_LETTERS,
                          BEGIN_LOWER_CASE_SPECIAL_LETTERS, END_LOWER_CASE_SPECIAL_LETTERS,
                          BEGIN_NUMBERS, END_NUMBERS,
                          CR, LF, SPACE)


def is_letter_or_number(character):
    byte_list = list(character.encode('utf-8'))
    new_char = byte_list[-1]
    return ((BEGIN_NUMBERS <= new_char <= END_NUMBERS) or
            (BEGIN_CAPITAL_LETTERS <= new_char <= END_CAPITAL_LETTERS) or
            (BEGIN_LOWER_CASE_LETTERS <= new_char <= END_LOWER_CASE_LETTERS) or
            (BEGIN_LOWER_CASE_SPECIAL_LETTERS <= new_char <= END_LOWER_CASE_SPECIAL_LETTERS) or
            (BEGIN_CAPITAL_SPECIAL_LETTERS <= new_char <= END_CAPITAL_SPECIAL_LETTERS))


def is_space_or_linebreak(character):
    byte_list = list(character.encode('utf-8'))
    return byte_list[-1] in [CR, LF, SPACE]


def is_punctuation(character):
    return (not is_letter_or_number(character) and not is_space_or_linebreak(character))
