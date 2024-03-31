
import sys
import pandas as pd
import math
import tertools
from collections import Counter

# Function to calculate Inverse Document Frequency (IDF) for each term
def calculate_idf(data):
    # Count the number of documents containing each term
    doc_freq = Counter()
    for tokens in data['tokens']:
        doc_freq.update(set(tokens))
    # Calculate IDF for each term
    num_documents = len(data)
    idf = {term: math.log(num_documents / (freq + 1)) for term, freq in doc_freq.items()}
    return idf

# Load preprocessed data
preprocessed_data_path = '/content/drive/My Drive/preprocessed_data.csv'
preprocessed_data = pd.read_csv(preprocessed_data_path)

# Calculate IDF
term_idf = calculate_idf(preprocessed_data)

# Add IDF values to the preprocessed_data DataFrame
preprocessed_data['idf'] = preprocessed_data['tokens'].apply(lambda tokens: {term: term_idf[term] for term in set(tokens)})

# Check the DataFrame to verify the 'idf' column
print(preprocessed_data.head())

# Now extract term frequencies
def extract_term_frequencies(data, document_id):
    document_row = data[data['ARTICLE_ID'] == document_id]
    term_frequencies = dict(zip(document_row['tokens'], document_row['idf']))
    return term_frequencies

# Represent each document with its term frequencies
document_term_frequencies = {}
for doc_id in preprocessed_data['ARTICLE_ID'].unique():
    document_term_frequencies[doc_id] = extract_term_frequencies(preprocessed_data, doc_id)

# Display the term frequencies for each document
for doc_id, term_freqs in document_term_frequencies.items():
    print(f"Document {doc_id} Term Frequencies:")
    # Convert the dictionary to a list of tuples and slice it
    term_freqs_list = list(term_freqs.items())[:50]
    print(term_freqs_list)

# Display only the first 5 rows
print(preprocessed_data.head())

# Display only the first 10 rows
print(preprocessed_data.head(10))

