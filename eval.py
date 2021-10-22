#!/usr/bin/env python

import argparse
import re


def main(args: argparse.Namespace) -> None:
    with open(args.predictions, "r") as source:
        regexp_h = re.compile(r"[H]-\d+")
        regexp_t = re.compile(r"[T]-\d+")
        h_data = []
        t_data = []
        errors = 0
        for line in source:
            items = line.split("\t")
            if regexp_h.search(items[0]):
                h_data.append(items)
            if regexp_t.search(items[0]):
                t_data.append(items)
        for x, y in zip(h_data, t_data):
            if x[2] != y[1]:
                errors += 1
        print("WER:", errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", help="path to input .txt file")
    main(parser.parse_args())
