import pandas as pd
import os
from config import Config
from logger.logger import logger


class Db:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.read_data()

    def read_data(self):
        try:
            logger.info("Reading csv file {}".format(self.filename))
            file_path = os.getcwd() + '/db/' + self.filename
            df = pd.read_csv(file_path, delimiter=',')
            df = df.reset_index()
            self.data = df
        except FileNotFoundError:
            logger.error("File {} not found".format(self.filename))
            self.data = pd.DataFrame([])

    def get_data(self, filter_by_brand_name=Config.brand_name):
        return self.data[(self.data.BrandName == filter_by_brand_name)].to_dict('records')







