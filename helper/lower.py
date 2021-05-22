from helper.const import BEGIN_CAPITAL_LETTERS, END_CAPITAL_LETTERS, BEGIN_CAPITAL_SPECIAL_LETTERS, END_CAPITAL_SPECIAL_LETTERS


def to_lower_regular_character(character):
    if (BEGIN_CAPITAL_LETTERS <= character <= END_CAPITAL_LETTERS):
        return character + 32
    return character


def to_lower_special_character(character):
    if (BEGIN_CAPITAL_SPECIAL_LETTERS <= character <= END_CAPITAL_SPECIAL_LETTERS):
        return character + 32
    return character
