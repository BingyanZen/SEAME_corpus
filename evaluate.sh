#!/bin/bash
# Evaluate POS tagging: pos.py tagger_output.py

# Usage: python tagger_output.py <number of source files: 1/2> <source file1><source file2> <gold file> <output file>
python tagger_output.py 2 universal_tagged_seame_d1.txt universal_tagged_seame_d2.txt extract_golden.txt output.txt
# python tagger_output.py 1 sample1.txt extract_golden.txt output.txt


# python pos.py <tagger_output file> <gold file>
python pos.py output.txt extract_golden.txt ../SEAME_corpus/poseval_result.txt