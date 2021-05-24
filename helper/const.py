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

artigos = ['o', 'os', 'a', 'as', 'um', 'uns', 'uma', 'umas', 'ao', 'aos', 'à', 'às', 'de', 'do', 'dos', 'da', 'das', 'dum', 'duns',
           'duma', 'dumas', 'em', 'no', 'nos', 'na', 'nas', 'num', 'nuns',	'numa', 'numas', 'por', 'per', 'pelo', 'pelos', 'pela', 'pelas']
pronomes_1 = ['eu', 'me', 'mim', 'comigo', 'tu', 'você', 'te', 'ti', 'contigo', 'ele', 'ela', 'o', 'a', 'lhe', 'se', 'si',
              'consigo', 'nós', 'nos', 'conosco', 'vós', 'vocês', 'vos', 'convosco', 'eles', 'elas', 'os', 'as', 'lhes', 'se', 'si', 'consigo']
pronomes_2 = ['meu', 'minha', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'seu', 'sua', 'seus', 'suas',
              'nosso', 'nossa', 'nossos', 'nossas', 'vosso', 'vossa', 'vossos', 'vossas', 'seu', 'sua', 'seus', 'suas']
pronomes_3 = ['esta', 'essa', 'aquela', 'estas', 'essas', 'aquelas', 'este',
              'esse', 'aquele', 'estes', 'esses', 'aqueles', 'isto', 'isso', 'aquilo']
pronomes_4 = ['algum', 'alguma', 'alguns', 'algumas', 'nenhum', 'nenhuma', 'nenhuns', 'nenhumas', 'muito', 'muita', 'muitos', 'muitas', 'pouco', 'pouca', 'poucos', 'poucas', 'todo', 'toda', 'todos', 'todas', 'outro', 'outra', 'outros',
              'outras', 'certo', 'certa', 'certos', 'certas', 'vário', 'vária', 'vários', 'várias', 'tanto', 'tanta', 'tantos', 'tantas', 'quanto', 'quanta', 'quantos', 'quantas', 'qualquer', 'quaisquer', 'qual', 'quais', 'um', 'uma', 'uns', 'umas']
pronomes_5 = ['quem', 'alguém', 'ninguém',
              'tudo', 'nada', 'outrem', 'algo', 'cada']
pronomes_6 = ['cujo', 'cuja', 'cujos', 'cujas', 'quanto',
              'quanta', 'quantos', 'quantas', 'quem', 'que', 'onde']
pronomes_7 = ['qual', 'quais', 'quanto',
              'quantos', 'quanta', 'quantas', 'quem', 'que']

pronomes = [*pronomes_1, *pronomes_2, *pronomes_3, *
            pronomes_4, *pronomes_5, *pronomes_6, *pronomes_7]

preposicoes = ['a', 'ante', 'após', 'até', 'com', 'conforme', 'contra', 'consoante', 'de', 'desde', 'durante',
               'em', 'excepto', 'entre', 'mediante', 'para', 'perante', 'por', 'salvo', 'sem', 'segundo', 'sob', 'sobre', 'trás']

palavras_ignoradas = [*artigos, *pronomes, *preposicoes, 'e']
