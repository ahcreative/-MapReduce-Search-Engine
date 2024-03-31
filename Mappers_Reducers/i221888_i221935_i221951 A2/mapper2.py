import sys
from collections import Counter
import math

def second_mapper(word, docID, tf, total_docs):
    # Emit intermediate key-value pairs of the form (word, (docID, TF, IDF))
    # Calculate IDF for the word
    idf = math.log10(total_docs / len(tf))
    yield word, (docID, tf, idf)

def second_reducer(intermediate):
    index_entries = defaultdict(list)
    # Aggregate the TF/IDF scores for each term in each document
    for word, (docID, tf, idf) in intermediate:
        index_entries[word].append((docID, tf * idf))

    # Output final index entries for each term, containing the TF/IDF scores and document IDs
    for word, entries in index_entries.items():
        yield word, entries
