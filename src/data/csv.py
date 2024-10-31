import os
import pandas as pd


class CSVData(list):
    def __init__(self, csv_path, data_generator=lambda: []):
        self.csv_path = csv_path
        self.data_generator = data_generator
        self.data = self.load_data()
        self.save_data_to_csv()

        super().__init__(self.data)

    def load_data(self):
        if os.path.exists(self.csv_path):
            return self.read_csv()
        return self.data_generator()

    def read_csv(self, value=dict):
        df = pd.read_csv(self.csv_path)
        return df.to_dict(orient="records")

    def save_data_to_csv(self):
        path = os.path.join(os.getcwd(), self.csv_path)
        df = pd.DataFrame(self.data)
        df.to_csv(path, index=False)
