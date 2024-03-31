from collections import defaultdict

# Load data from a file
file_path = '/home/laiba/Downloads/preprocessed_data.csv'
with open(file_path, 'r') as file:
    documents = file.readlines()

# Apply mapper function to each document
intermediate_results = []
for document in documents:
    intermediate_results.extend(mapper(document))

# Apply reducer function to aggregate results
final_results = reducer(intermediate_results)

# Apply second mapper function to each result from the first reducer
second_intermediate_results = []
for word, entries in final_results:
    for entry in entries:
        docID, tf = entry
        second_intermediate_results.extend(second_mapper(word, docID, tf, total_docs))

# Apply second reducer function to aggregate results
final_index_entries = second_reducer(second_intermediate_results)
