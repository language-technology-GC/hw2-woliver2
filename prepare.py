#!/usr/bin/env python

import argparse
import pandas as pd


def main(args: argparse.Namespace) -> None:
    with open(args.ice_data, "r") as source:
        df = pd.read_csv(source, sep="\t", header=None)
        col1_list = []
        for i in df[0]:
            col1_list.append(" ".join(i))
        for line in col1_list:
            print(line, file=args.gfile)
        for line in df[1]:
            print(line, file=args.pfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ice_data", help="path to input .tsv file")
    parser.add_argument(
        "gfile", type=argparse.FileType("w"), help="path to output .g file"
    )
    parser.add_argument(
        "pfile", type=argparse.FileType("w"), help="path to output .p file"
    )
    main(parser.parse_args())
