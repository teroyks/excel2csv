# Excel to CSV Converter

Simple converter to save all the sheets in an Excel file to CSV files.

## Installation

You need Python 3 with the following packages – install globally or with [virtualenv](https://realpython.com/python-virtual-environments-a-primer/).

    pip3 install pandas
    pip3 install xlrd
    pip3 install tqdm

Just download the files and run `excel2csv`.

## Usage

```shell
excel2csv [-h] [-d DELIMITER] [-f] excel_file

positional arguments:
  excel_file            input file

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        CSV delimiter
  -f, --force           force overwriting existing CSV files
```
