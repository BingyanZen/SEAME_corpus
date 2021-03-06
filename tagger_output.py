import sys

def main():
    if len(sys.argv) < 4:
	print "Usage: python tagger_output.py <number of source files: 1/2> <source file1><source file2> <gold file> <output file>"
	exit(1)

    counter = int(sys.argv[1])

    if counter == 2:
        infile = open(sys.argv[2], "r")
        dev_sentences = infile.readlines()
        infile.close()

        infile = open(sys.argv[3], "r")
        dev_sentences += infile.readlines()
        infile.close()

        infile = open(sys.argv[4], "r")
        gold_sentences = infile.readlines()
        infile.close()

        outfile = open(sys.argv[5], "w")
    
    if counter == 1:
        infile = open(sys.argv[2], "r")
        dev_sentences = infile.readlines()
        infile.close()

        infile = open(sys.argv[3], "r")
        gold_sentences = infile.readlines()
        infile.close()

        outfile = open(sys.argv[4], "w")


    num_correct = 0
    total = 0

    outfile_list = []

    for gold_sent in gold_sentences:
        total += 1
        gold_tok = gold_sent.split()
        gold_key = gold_tok[:3]

        for dev_sent in dev_sentences:
            dev_tok = dev_sent.split()
            dev_key = dev_tok[:3]
            if dev_key == gold_key:
                outfile_list += dev_sent

    outfile.writelines(outfile_list)
    outfile.close()


if __name__ == "__main__": main()