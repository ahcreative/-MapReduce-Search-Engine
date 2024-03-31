# -MapReduce-Search-Engine

# Introduction
This repository contains the code and documentation for Assignment 2 of the "Fundamentals of Big Data Analytics" course (DS2004). The assignment focuses on developing a basic search engine using Apache Hadoop's MapReduce framework.


# Dataset
For this assignment, a portion of the English Wikipedia dump provided by Wikimedia will be used, containing around 5 million Wikipedia articles. The dataset includes the following fields:
- `ARTICLE_ID`: int, serves as the identifier for each unique title.
- `TITLE`: str, denotes the titles of articles.
- `SECTION_TITLE`: str, represents subsection titles from each article.
- `SECTION_TEXT`: str, contains text from each subsection.

# Developing a Naïve Search Engine Utilizing MapReduce
- The objective is to develop a basic search engine using Apache Hadoop's MapReduce.
- The search engine should be capable of processing queries and delivering a list of the most relevant documents.
- The assignment involves implementing both document indexing and query processing using the MapReduce paradigm.

# Technology
- Utilize Apache Hadoop's MapReduce framework for document indexing and query processing.
- Implement the TF/IDF Vector Space model for relevance calculation.
- Organize the project using a public GitHub repository with incremental commits to track progress.

# Dataset Description and Processing
- Thoroughly review Apache’s MapReduce Tutorial for basic text cleaning and processing.
- Focus on the `ARTICLE_ID` and `SECTION_TEXT` columns for indexing and query processing.

# Testing and Deployment
- Conduct local testing on a smaller dataset to accelerate the development process.
- Deploy the search application using Hadoop's MapReduce framework.
- Provide methods to run the indexer and execute queries with specified arguments.

# Part 1: Preprocessing the Dataset

# Introduction
In this part of the assignment, we perform preprocessing on the dataset to prepare it for indexing and query processing in the search engine.

#### Steps:
1. **Loading the Data:** The dataset is loaded from a CSV file, and only the first 500 rows are loaded for initial processing.

2. **Basic Text Cleaning:** We perform basic text cleaning to remove HTML tags and convert the text to lowercase.

3. **Tokenization:** The cleaned text is tokenized into individual words using the NLTK library's word_tokenize function.

4. **Removing Stopwords:** Stopwords, such as 'the', 'is', 'and', etc., are removed from the tokenized text to reduce noise in the data.

5. **Stemming and Lemmatization:** We apply stemming and lemmatization techniques to reduce words to their root forms, improving the efficiency of the search engine.

6. **Saving Preprocessed Data:** The preprocessed data is saved to a new CSV file for further processing.


# Part 2 Mapper and Reducer

This part contains Python scripts for implementing the Map-Reduce approach for creating an inverted index. The inverted index is a data structure used in information retrieval systems to facilitate efficient text search operations.

## Overview

The Map-Reduce approach consists of two main phases: the Map phase and the Reduce phase. In the Map phase, the input data is processed and transformed into intermediate key-value pairs. In the Reduce phase, these intermediate key-value pairs are aggregated and combined to produce the final output.

This repository contains the following scripts:

1. `mapper1.py`: This script implements the Map phase of the first step. It tokenizes the input documents, counts the frequency of each word in each document, and emits intermediate key-value pairs of the form `(word, docID)`.

2. `reducer1.py`: This script implements the Reduce phase of the first step. It takes the intermediate key-value pairs from the Map phase and calculates the term frequency (TF) for each word in each document. It then emits intermediate key-value pairs of the form `(word, (docID, TF))`.

3. `mapper2.py`: This script implements the Map phase of the second step. It takes the intermediate key-value pairs from the first Reduce phase and calculates the inverse document frequency (IDF) for each word. It then emits intermediate key-value pairs of the form `(word, (docID, TF, IDF))`.

4. `reducer2.py`: This script implements the Reduce phase of the second step. It takes the intermediate key-value pairs from the second Map phase and aggregates the TF/IDF scores for each term in each document. It then outputs the final index entries for each term, containing the TF/IDF scores and document IDs.

5. `mapper3.py`: This script is an example of how to load and tokenize the input data (queries) for the information retrieval system.

6. `reducer3.py`: This script calculates the inverse document frequency (IDF) for each term in the preprocessed data. It then combines the term frequencies (TF) and IDF values to represent each document with its term frequencies. This can be used for further processing or ranking in the information retrieval system.

7. `IDF File (idf.txt):`
   - This file contains the inverse document frequency (IDF) values calculated for each term in the dataset. IDF values are essential for determining the importance of terms in the search engine's indexing and query processing.

8. `TF File (tf.txt):`
   - The TF file contains the term frequency (TF) values calculated for each term in each document. TF values represent the frequency of occurrence of each term within a document and play a crucial role in relevance calculation.

9. `Term IDF File (term_idf.txt):`
   - This file stores the term frequency-inverse document frequency (TF-IDF) scores for each term in each document. TF-IDF scores combine the TF and IDF values to measure the importance of a term in a document relative to the entire dataset.

10. `Query File (query.txt):`
    - The query file contains queries that can be used to test the search engine. Each query is provided in a separate line, and the search engine can process these queries to retrieve relevant documents based on their content.


