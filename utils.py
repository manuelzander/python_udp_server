#!/usr/bin/env python

from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Emoji app")
    parser.add_argument(
        "--n", default=1, 
        type=int, 
        required=False, 
        help="Multiply number of emojis by n",
    )
    parser.add_argument(
        "--s",
        default="",
        type=str,
        required=False,
        help="Separator between each emoji",
    )
    parser.add_argument(
        "--r",
        default=False,
        type=bool,
        required=False,
        help="Disable the translation from keyword to emoji",
    )
    return parser
