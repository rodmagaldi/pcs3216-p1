USUAL_OFFSET = 32

BEGIN_CAPITAL_LETTERS = 65
END_CAPITAL_LETTERS = 90

BEGIN_LOWER_CASE_LETTERS = BEGIN_CAPITAL_LETTERS + USUAL_OFFSET
END_LOWER_CASE_LETTERS = END_CAPITAL_LETTERS + USUAL_OFFSET

BEGIN_CAPITAL_SPECIAL_LETTERS = 128
END_CAPITAL_SPECIAL_LETTERS = 156

BEGIN_LOWER_CASE_SPECIAL_LETTERS = BEGIN_CAPITAL_SPECIAL_LETTERS + USUAL_OFFSET
END_LOWER_CASE_SPECIAL_LETTERS = END_CAPITAL_SPECIAL_LETTERS + USUAL_OFFSET

BEGIN_NUMBERS = 48
END_NUMBERS = 57

CR = 13
LF = 10
SPACE = 32

a_array = ['à', 'á', 'â', 'ã', 'ä']
e_array = ['è', 'é', 'ê', 'ë']
i_array = ['ì', 'í', 'î', 'ï']
o_array = ['ò', 'ó', 'ô', 'õ', 'ö']
u_array = ['ù', 'ú', 'û', 'ü']

special_vowels_array = [*a_array, *e_array, *i_array, *o_array, *u_array]

special_char_dict = {
    'a': a_array,
    'e': e_array,
    'i': i_array,
    'o': o_array,
    'u': u_array
}
