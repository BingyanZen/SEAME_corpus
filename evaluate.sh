#!/bin/bash
# Evaluate POS tagging: pos.py tagger_output.py

# python tagger_output.py <d1 file> <d2 file> <gold file> <output file>
python tagger_output.py universal_tagged_seame_d1.txt universal_tagged_seame_d2.txt extract_golden.txt output.txt

# python pos.py <tagger_output file> <gold file>
python pos.py output.txt extract_golden.txt