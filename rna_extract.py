#!/usr/bin/env python

from __future__ import print_function

import argparse
from Bio import SeqIO
from ncbi_acc_download.core import (
    Config,
    download_to_file
)
import os


def main():
    parser = argparse.ArgumentParser(description="Extract tRNA and rRNA features from a sequence specified by NCBI GenBank ID")
    parser.add_argument("ncbi_id", help="NCBI GenBank ID to extract RNA features from.")
    parser.add_argument("--reuse", action="store_true", default=False,
                        help="Reuse exising file if available")

    args = parser.parse_args()

    # Download file in GenBank format
    # Could download into a StringIO buffer by using the
    # ncbi_acc_download.download functions directly, but then we can't --reuse
    filename = "{}.gbk".format(args.ncbi_id)
    if not os.path.isfile(filename):
        cfg = Config(recursive=True, format="genbank", out=filename)
        download_to_file(args.ncbi_id, cfg, filename)

    # Extract RNA features
    records = list(SeqIO.parse(filename, "genbank"))
    for record in records:
        for feature in record.features:
            if feature.type not in ("tRNA", "rRNA"):
                continue
            # this crashes if there is no locus tag, but NCBI genomes should have these
            locus_tag = feature.qualifiers['locus_tag'][0]
            header = ">{type}|{locus_tag}".format(type=feature.type, locus_tag=locus_tag)
            seq = feature.extract(record.seq)
            print(header, seq, sep='\n')


if __name__ == "__main__":
    main()
