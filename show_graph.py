#!/usr/bin/python3

# Example:
# python3 Analysis/show_graph.py -f voo.csv,nvda.csv -p voo,nvda -v close

from matplotlib import pyplot as plt
import pandas as pd
import datetime
from optparse import OptionParser


def parse_input_files(filenames, products):
    dct = {}
    for filename, product in zip(filenames, products):
        df = pd.read_csv(filename)
        df['datetime'] = df['date'].apply(
                lambda date: datetime.datetime.strptime(date, '%Y/%m/%d'))
        dct[product] = df
    return dct


def display(dataframes_dct, values):
    for product, df in dataframes_dct.items():
        for value in values:
            plt.plot(df['datetime'],
                     df[value],
                     label="{}_{}".format(product, value))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--files', dest='files',
                      help='input filenames (comma sepperated)')

    parser.add_option('-p', '--products', dest='products',
                      help='names of products (comma sepperated)')

    parser.add_option('-v', '--values', dest='values',
                      help='Which field values to show from csv')

    parser.add_option('-d', '--display_values', action='store_true',
                      dest='display_values',
                      help='Display available fields and exit')

    (options, args) = parser.parse_args()

    dataframes_dct = parse_input_files(options.files.split(','),
                                       options.products.split(','))

    if options.display_values:
        print('Not implemented')
        quit()

    display(dataframes_dct, options.values.split(','))
