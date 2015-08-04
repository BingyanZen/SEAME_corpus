import codecs
import sys

def main():
    if len(sys.argv) < 3:
	print "Usage: python pos.py <tagger output> <reference file> <path to output file>"
	exit(1)

    infile = codecs.open(sys.argv[1], "r", 'utf-8')
    user_sentences = infile.readlines()
    infile.close()

    infile = codecs.open(sys.argv[2], "r", 'utf-8')
    correct_sentences = infile.readlines()
    infile.close()

    num_correct = 0
    total = 0

    f = codecs.open(sys.argv[3], 'w', 'utf-8')

    for user_sent, correct_sent in zip(user_sentences, correct_sentences):
        user_tok = user_sent.split()
        correct_tok = correct_sent.split()
        user_tok = user_tok[3:]
        correct_tok = correct_tok[3:]
        len_c = 0
        num_incorrect = 0

        if len(user_tok) != len(correct_tok):
            continue

        for u, c in zip(user_tok, correct_tok):
            if u == c:
                num_correct += 1
            elif u != c:
                num_incorrect +=1
                f.write("dev tok: " + ''.join(u))
                f.write("    ")
                f.write("gold tok: " + ''.join(c))
                f.write("\n")
            len_c += 1
            total += 1

        if num_correct != 0 and len_c  == len(user_tok):
            f.write("dev sentence: " + ' '.join(user_tok))
            f.write("\n")
            f.write("gold sentence: " + ' '.join(correct_tok))
            f.write("\n\n")

    f.close()
    
    score = float(num_correct) / total * 100

    print "Percent correct tags:", score


if __name__ == "__main__": main()
