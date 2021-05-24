import pandas as pd


class ResultHandler:
    def __init__(self, results_dict, save_path):
        self.results_dict = results_dict
        self.save_path = save_path
        self.results_dataframe = None
        self.total_words = None
        self.total_identified_words = None

    def configure_pd(self):
        self.results_dataframe = pd.DataFrame.from_dict(
            self.results_dict, orient='index')
        pd.set_option('display.max_rows', None)

    def save_results(self):
        self.configure_pd()
        self.total_words = self.results_dataframe.sum(axis=0)['count']
        print(self.total_words)
        self.results_dataframe = self.results_dataframe[self.results_dataframe['keyword'] == True]
        self.total_identified_words = self.results_dataframe.sum(axis=0)[
            'count']
        print(self.total_identified_words)
        print("{:.2f}".format(
            100 * self.total_identified_words / self.total_words), "%")
        self.results_dataframe.to_csv(self.save_path, index=True)

    def show_results(self):
        print(self.results_dataframe)
