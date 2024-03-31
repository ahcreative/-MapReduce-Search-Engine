# Load data from a file
file_path = '/home/laiba/Downloads/preprocessed_data.csv'
with open(file_path, 'r') as file:
    documents = file.readlines()

# Apply mapper function to each document
intermediate_results = []
for document in documents:
    intermediate_results.extend(mapper(document))

# Apply reducer function to aggregate results
final_results = reducer(intermediate_result
