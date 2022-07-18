import sys
import logging
import argparse
import csv
from .utils import get_log_filename

logging.basicConfig(filename=get_log_filename('detransliterator.csv_tool'), level=logging.DEBUG)

def main_parse_command_line_args():
    parser = argparse.ArgumentParser("CSV File Manipulation Tools")
    parser.add_argument("option", choices=["extract-column", "insert-column"])

    parser.add_argument("--skip-lines", type=int, default=0)
    parser.add_argument("--column-ix", type=int, required=True)

    parser.add_argument("--csv-formatting-params", nargs="*", default=[])
    # https://docs.python.org/3/library/csv.html#csv-fmt-params

    return parser.parse_args()


def parse_csv_formatting_params(args):
    if len(args.csv_formatting_params) %2 != 0:
        raise ValueError(
            "--csv-formatting-params must be specified in pairs: "
            "parameter1-name parameter1-value parameter2-name parameter2-value ..."
        )
    csv_reader_kwargs = {}
    i=0
    while i<len(args.csv_formatting_params):
        key = args.csv_formatting_params[i]
        i+=1
        value = args.csv_formatting_params[i]
        i+=1
        csv_reader_kwargs[key] = value

    if "delimiter" in csv_reader_kwargs:
        if csv_reader_kwargs["delimiter"] == 'tab':
            csv_reader_kwargs["delimiter"] = '\t'
            
    return csv_reader_kwargs


def main_extract_csv_column(args):
    if args.column_ix is None:
        raise ValueError("--column-ix required for extraction")
    csv_reader_kwargs = parse_csv_formatting_params(args)
    reader = csv.reader(sys.stdin, **csv_reader_kwargs)
    row_ix = -1
    for row in reader:
        row_ix += 1
        if row_ix < args.skip_lines:
            continue
        cell = row[args.column_ix]
        print(cell)


def main_insert_csv_column(args):
    raise NotImplementedError()

if __name__ == '__main__':
    args = main_parse_command_line_args()
    if args.option == 'extract-column':
        main_extract_csv_column(args)
    elif args.option == 'insert-column':
        main_insert_csv_column(args)
    else:
        raise ValueError(f"Unknown command: {args.option}")
