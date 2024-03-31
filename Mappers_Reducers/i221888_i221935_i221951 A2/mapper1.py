import sys
import re

def mapper(document):
    try:
        docID, text = document.strip().split('\t')  # Assuming the document format is "<docID>\t<text>"
        words = re.findall(r'\b\w+\b', text.lower())  # Tokenize the document and convert to lowercase
        word_count = {}  # Dictionary to store word counts for the document
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        # Emit intermediate key-value pairs of the form (word, docID)
        for word, count in word_count.items():
            yield (word, docID), count
    except ValueError:
        # Handle cases where the line doesn't have the expected format
        print("Skipping line:", document)


def reducer(intermediate):
    word_doc_count = defaultdict(dict)  # Dictionary to store word counts for each document
    for key, count in intermediate:
        word, docID = key
        if word not in word_doc_count:
            word_doc_count[word] = {}
        word_doc_count[word][docID] = count

    # Calculate TF and emit intermediate key-value pairs of the form (word, (docID, TF))
    for word, doc_counts in word_doc_count.items():
        total_words_in_doc = sum(doc_counts.values())
        for docID, count in doc_counts.items():
            tf = count / total_words_in_doc
            yield word, (docID, tf)
