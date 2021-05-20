from runner import Runner
from result_handler import ResultHandler

keywords_list = ['o', 'Então', 'ali', ',']
runner = Runner(input_file_path='teste_novo.txt', keywords=keywords_list)
results = runner.run()
handler = ResultHandler(results_dict=results, save_path='teste_novo.csv')
handler.save_results()
handler.show_results()
handler.show_keywords_results()
