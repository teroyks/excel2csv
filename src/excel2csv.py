import argparse
import pandas as pd

from tqdm import tqdm

parser = argparse.ArgumentParser(description='Excel to CSV converter')
parser.add_argument('excel_file', type=argparse.FileType(
    mode='r'), help='input file')

args = parser.parse_args()
filename = args.excel_file.name

file = pd.ExcelFile(filename)
sheets = file.sheet_names

for sheet in tqdm(sheets):
    pass
