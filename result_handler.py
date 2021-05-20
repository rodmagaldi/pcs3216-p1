import pandas as pd


class ResultHandler:
    def __init__(self, results_dict, save_path):
        self.results_dict = results_dict
        self.save_path = save_path
        self.results_dataframe = None

    def configure_pd(self):
        self.results_dataframe = pd.DataFrame.from_dict(
            self.results_dict, orient='index')
        pd.set_option('display.max_rows', None)

    def save_results(self):
        self.configure_pd()
        self.results_dataframe.to_csv(self.save_path, index=True)

    def show_results(self):
        print(self.results_dataframe)

    def show_keywords_results(self):
        print(
            self.results_dataframe[self.results_dataframe['keyword'] == True])
