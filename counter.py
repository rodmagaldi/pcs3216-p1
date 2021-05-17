from runner import Runner
from result_handler import ResultHandler

keywords_list = ['o', 'Então', 'ali', ',']
runner = Runner('teste.txt', keywords_list)
results = runner.run()
handler = ResultHandler(results, 'teste.csv')
handler.save_results()
handler.show_results()
handler.show_keywords_results()