import sys
from io import StringIO
import argparse
import logging
from .utils import get_log_filename

logging.basicConfig(filename=get_log_filename('detransliterator.tool'), level=logging.DEBUG)

from .detransliterator import Detransliterator


def main_parse_command_line_args():
    parser = argparse.ArgumentParser("latin to nqo detransliterator")
    parser.add_argument("--model-name", required=True)
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

    detransliterator = Detransliterator(args.model_name)

    sys.stdout = std_out_bkp
    for latin_line in sys.stdin:
        nqo_line = detransliterator.detransliterate(
            latin_line,
            beam_size=args.beam_size
        )
        print(nqo_line)


if __name__ == '__main__':
    args = main_parse_command_line_args()
    if True:  # args.option == 'command-name':
        main_detransliterate(args)
    else:
        raise ValueError(f"Unknown command: {args.option}")
