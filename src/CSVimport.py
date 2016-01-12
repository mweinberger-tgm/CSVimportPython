import csv

class CSVimport(object):

    """

    """
    def readCSV(self):

        with open('SalesJan2009.csv', newline='') as f:
            reader = csv.reader(f)
        for row in reader:
            print(row)
