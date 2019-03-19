import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Excel to CSV converter')
parser.add_argument('excel_file', type=argparse.FileType(
    mode='r'), help='input file')

args = parser.parse_args()
filename = args.excel_file.name

contents = pd.read_excel(filename)
