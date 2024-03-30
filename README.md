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
