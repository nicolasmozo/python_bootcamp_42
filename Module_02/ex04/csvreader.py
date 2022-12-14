import csv
import pandas as pd
import os


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        if not os.path.exists(self.filename):
            return None
        df = pd.read_csv(self.filename, sep=self.sep)
        headers = df.head(1).count(axis=1)
        if headers[0] < len(df.columns):
            return print('Line with too many values')
        if df.isnull().values.any():
            return print('Line with too few values')
        return self

    def __exit__(self, type, value, traceback):
        if type == AttributeError:
            print('File does not exist')
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        if self.header == True:
            ls = []
            for i in range(1, self.skip_top + 1):
                ls.append(i)
            df = pd.read_csv(self.filename, sep=self.sep, skiprows=ls)
            return df[:len(df)-self.skip_bottom]
        else:
            df = pd.read_csv(self.filename, sep=self.sep,
                             skiprows=self.skip_top)
            return df[:len(df)-self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
        None: (when self.header is False)."""
        if self.header == True:
            df = pd.read_csv(self.filename, sep=self.sep)
            return df.head(1)
        else:
            return None
