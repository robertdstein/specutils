#!/usr/bin/env python
import argparse
import logging
from pathlib import Path
from specutils.clean import clean_spectrum, recogned_suffix
from specutils.classify import run_snid

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="specutils: Utils for spectroscopy"
)

parser.add_argument(
    "-d",
    "--directory",
    default=Path.cwd(),
    help="Sub-directory to use in the data directory"
)

parser.add_argument(
    "-f",
    "--file",
    help="File to reduce",
    default=None
)

args = parser.parse_args()

data_dir = args.directory
if isinstance(data_dir, str):
    data_dir = Path(data_dir)

if args.file is None:
    file_paths = [x for x in data_dir.glob('*') if x.suffix in recogned_suffix]
else:
    file_paths = [data_dir.joinpath(args.file)]

print(file_paths)

for file_path in file_paths:

    print(file_path)

    # Clean spectrum to make it readable by snid
    clean_path = clean_spectrum(file_path)

    # Run snid (assuming it is installed)
    run_snid(clean_path)
