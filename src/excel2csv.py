import argparse
import pandas as pd
import os

from tqdm import tqdm


def sanitize_filename(str):
    return "".join(char for char in str if char.isalnum())


parser = argparse.ArgumentParser(description='Excel to CSV converter')
parser.add_argument('excel_file', type=argparse.FileType(
    mode='r'), help='input file')
parser.add_argument('-d', '--delimiter', default=',',
                    type=str, help='CSV delimiter')

args = parser.parse_args()
filename = args.excel_file.name
basename, _ = os.path.splitext(filename)

excel_file = pd.ExcelFile(filename)
sheets = excel_file.sheet_names

sheet_files = []
for sheet in tqdm(excel_file.sheet_names):
    sheet_filename = f'{basename}_{sanitize_filename(sheet)}.csv'
    try:
        csv_file = open(sheet_filename, 'x')
    except Exception as e:
        print(f'Cannot write to {sheet_filename} - {e}')
    else:
        with csv_file:
            df = excel_file.parse(sheet_name=sheet)
            for _, row in tqdm(df.iterrows(), total=len(df.index)):
                row_values = []
                for _, val in row.iteritems():
                    row_values.append(str(val))
                print(args.delimiter.join(row_values), file=csv_file)
            sheet_files.append(sheet_filename)

print()
if len(sheet_files):
    print('Created CSV files: \n' +
          "".join(f'{csv_file}\n' for csv_file in sheet_files))
else:
    print('No CSV files created.')
