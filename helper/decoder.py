def decode_special_character(character, next_character):
    char_array = bytearray(bytes([character]))

    new_char_array = bytearray(bytes([next_character]))

    array = char_array + new_char_array
    decoded = array.decode('utf-8')
    return decoded


def decode_regular_character(character):
    return bytes([character]).decode('utf-8')
