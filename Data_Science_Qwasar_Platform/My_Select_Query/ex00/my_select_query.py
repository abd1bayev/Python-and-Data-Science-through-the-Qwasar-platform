import csv
import pandas as pd
from io import StringIO

class MySelectQuery:
    def __init__(self, mazmuni):

        mazmuni = mazmuni.split('\n')
        column = mazmuni[0].split(',')
        mazmuni = [row.split(',') for row in mazmuni[1:-1]]
        mazmuni[-2] = mazmuni[-2][:-1]

        self.data = pd.DataFrame(mazmuni, columns = column)

    def where(self, column_name, criteria):
        result = self.data[self.data[column_name] == criteria].values
        result = ','.join(result[0])
        return [result]
