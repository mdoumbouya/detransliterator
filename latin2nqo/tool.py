import sys
from io import StringIO
import argparse
import csv
from .latin2nqo import get_model_by_name

def main_parse_command_line_args():
    parser = argparse.ArgumentParser("latin to nqo detransliterator")
    parser.add_argument("--model-name", required=False, default="001.35")
    parser.add_argument("--input-text-file")
    parser.add_argument("--input-csv-file")
    parser.add_argument("--input-csv-file-separator")
    parser.add_argument("--beam-size", type=int, required=False, default=5)
    return parser.parse_args()


def main_detransliterate(args):
    std_out_bkp = sys.stdout
    sys.stdout = StringIO()

    if not args.model_name:
        raise ValueError("--model-name required for detransliteration")
    model = get_model_by_name(args.model_name)

    sys.stdout = std_out_bkp
    for latin_line in sys.stdin:
        nqo_line = model.translate(latin_line, beam=args.beam_size)
        print(nqo_line)



if __name__ == '__main__':
    args = main_parse_command_line_args()
    if True: # args.option == 'command-name':
        main_detransliterate(args)
    else:
        raise ValueError(f"Unknown command: {args.option}")

