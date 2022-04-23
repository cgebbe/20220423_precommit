"""
see https://github.com/pre-commit/pre-commit-hooks/blob/main/pre_commit_hooks/check_yaml.py
"""

from __future__ import annotations

import argparse
from fileinput import filename
from typing import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    raise ValueError(f"{args.filenames=}")

import sys
main(sys.argv)