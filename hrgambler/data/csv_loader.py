import csv
import contextlib


class Loader(object):
    def __init__(self, path):
        self.path = path
        self.row_data = None
        self.csv_file = None

    @contextlib.contextmanager
    def data_load(self):
        self.csv_file = open(self.path, 'r')
        self.row_data = csv.reader(self.csv_file, delimiter=',', quotechar='"')

    def close_file(self):
        if self.csv_file is not None:
            self.csv_file.close()
