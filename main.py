from runner import Runner
from result_handler import ResultHandler
from string import punctuation
from helper.const import palavras_ignoradas

from classificador.listas import artes, futebol, politica

keywords_list = [*politica]
runner = Runner(input_file_path='classificador/politica.txt',
                keywords=keywords_list)
results = runner.run()
handler = ResultHandler(results_dict=results,
                        save_path='classificador/x.csv')
handler.save_results()
handler.show_results()
