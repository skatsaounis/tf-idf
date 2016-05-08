#!/usr/bin/env python
import sys
import re
from stemming.porter2 import stem


def termFreq(documents, term, stemming):
    documentsWithTerm = 0
    termAppearances = 0
    documentFlag = False

    for document in documents:
        wordList = re.sub("[^\w]", " ", document).split()

        for word in wordList:
            if stemming:
                if stem(term) in word:
                    documentFlag = True
                    termAppearances += 1
                    # print "\"%s\" contains term \"%s\"!" % (word, term)
            else:
                if term == word:
                    documentFlag = True
                    termAppearances += 1
                    # print "term \"%s\" has been found!" % (term)

        if documentFlag:
            documentsWithTerm += 1
            documentFlag = False

    print "--- Statistics ---"
    print "(%s) documents" % (len(documents))
    print "(%s) documents contain term \"%s\"" % (documentsWithTerm, term)
    print "(%s) appearances of term \"%s\"" % (termAppearances, term)


def main():
    if len(sys.argv) != 4:
        print "Usage: <input_file> <list_of_terms> <stemming_flag>"
        sys.exit(1)

    filename = sys.argv[1]
    term = sys.argv[2]
    stemming = int(sys.argv[3])

    if stemming != 0 and stemming != 1:
        print "Stemming Flag is either 0 or 1"
        sys.exit(1)

    txt = open(filename)
    documents = txt.read().split('\n\n')
    termFreq(documents, term, stemming)

if __name__ == "__main__":
    main()
