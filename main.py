from runner import Runner
from result_handler import ResultHandler
from string import punctuation
from helper.const import palavras_ignoradas

keywords_list = [*punctuation, *palavras_ignoradas]
runner = Runner(input_file_path='complementar/futebol.txt',
                keywords=keywords_list)
results = runner.run()
handler = ResultHandler(results_dict=results,
                        save_path='complementar/futebol.csv')
handler.save_results()
handler.show_results()
