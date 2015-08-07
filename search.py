import sys
import codecs

def __unicode__(self):
    return self

def count_POS_occurence(POStagstr, user_sentences):
    search_list = {}
    num = 0

    for sent in user_sentences:
        sent_tok = sent.split()
        for token in sent_tok:
            if token.find(POStagstr)>0:
                if token not in search_list:
                    search_list.update({token: 1})
                else:
                    search_list[token] += 1
                num +=1 
    return search_list, num


def count_WordList_occurence(wordlist, user_sentences):
    count_dict = {}

    for sent in user_sentences:
        sent_tok = sent.split()
        for token in sent_tok:
            if token in wordlist:
                if token not in count_dict:
                    count_dict.update({token: 1})
                else:
                    count_dict[token] +=1
    return count_dict

# def compare_sentence(keyword,sent1, sent2):
#     outputlist1 = []
#     outputlist2 = []
#     for sent in sent1:
#         sent_tok = sent.split()
#         for token in sent_tok:
#             if token.find(keyword)>0:
#                 outputlist1.append(sent)

#     for sent in sent2:
#         sent_tok = sent.split()
#         for token in sent_tok:
#             if token == keyword:
#                 outputlist2.append(sent)
#     return outputlist1, outputlist2


def main():

    # Argument
    if len(sys.argv) < 5:
	print "Usage: python search.py <tagsource file1><tagsource file2> <source file3><source file4>"
	exit(1)

    infile = codecs.open(sys.argv[1], "r", 'utf-8')
    tag_sentences = infile.readlines()
    infile.close()
    infile = codecs.open(sys.argv[2], "r", 'utf-8')
    tag_sentences += infile.readlines()
    infile.close()

    infile = codecs.open(sys.argv[3], "r", 'utf-8')
    sentences = infile.readlines()
    infile.close()
    infile = codecs.open(sys.argv[4], "r", 'utf-8')
    sentences += infile.readlines()
    infile.close()

    # Count the POS occurance for each word
    search_str = "INTJ"
    search_dict, total_num = count_POS_occurence(search_str, tag_sentences)
    for word, value in search_dict.iteritems():
        print word.encode('utf-8') + ": " + str(value)
    print total_num

    # Count the word occurence for the input wordlist
    wordList = ['yeah', 'yah', 'ya', 'right']
    for each in wordList:
        each = each.encode('utf-8')
    word_dict = count_WordList_occurence(wordList, sentences)
    for word, value in word_dict.iteritems():
        print word.encode('utf-8') + ": " + str(value)

    # key = "ya"
    # tagsentences_list, sentences_list = compare_sentence(key, tag_sentences, sentences)
    
    # for each1, each2 in zip(tagsentences_list, sentences_list):
    #     each1_tok = each1.split()
    #     each2_tok = each2.split()
    #     if (each1_tok[:3]) == (each2_tok[:3]):
    #         print 'tag: ' + each1.encode('utf-8') + '\n'
    #         print 'raw: ' + each2.encode('utf-8') + '\n'
    #     else:
    #         print 'tag: ' +each1

if __name__ == "__main__": main()