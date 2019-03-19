import argparse
import pandas as pd
import os

from tqdm import tqdm


def sanitize_filename(str):
    return "".join(char for char in str if char.isalnum())


parser = argparse.ArgumentParser(description='Excel to CSV converter')
parser.add_argument('excel_file', type=argparse.FileType(
    mode='r'), help='input file')

args = parser.parse_args()
filename = args.excel_file.name
basename, _ = os.path.splitext(filename)

file = pd.ExcelFile(filename)
sheets = file.sheet_names

sheet_files = []
for sheet in tqdm(file.sheet_names):
    sheet_filename = f'{basename}_{sanitize_filename(sheet)}.csv'
    try:
        file = open(sheet_filename, 'x')
    except Exception as e:
        print(f'Cannot write to {sheet_filename} - {e}')
    else:
        with file:
            print('foo', file=file)
            sheet_files.append(sheet_filename)

if len(sheet_files):
    print('Created CSV files: \n' +
          "".join(f'{csv_file}\n' for csv_file in sheet_files))
else:
    print('No CSV files created.')
