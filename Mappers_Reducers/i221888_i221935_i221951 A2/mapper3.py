import pandas as pd

# Load the CSV file containing queries
queries_file_path = '/home/laiba/Downloads/preprocessed_data.csv'
queries_data = pd.read_csv(queries_file_path)

# Print the column names to identify the correct column containing the queries
print("Column Names:", queries_data.columns)

 Define the tokenize_query function
def tokenize_query(query):
    # Tokenize the query here (replace this with your actual tokenization logic)
    return query.split()
# Apply tokenize_query function to each query in queries_data['tokens']
tokenized_queries = queries_data['tokens'].apply(tokenize_query)
print(tokenized_queries)

