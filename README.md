# Natural Language Processing

This repository contains my academic work and experiments related to **Natural Language Processing (NLP)** using Python.  
The focus is on understanding core NLP concepts through implementatio.

---

## Contents of the Repository

The repository consists mainly of Jupyter notebooks and a few Python scripts.  
Each file explores a specific NLP concept or technique.

### 1. Text Preprocessing
- **`Text Preprocessing.ipynb`**
  - Covers basic text cleaning steps such as:
    - Lowercasing
    - Remove HTML tags
    - Remove URLs
    - Remove Punctuation
    - Chat(Short) Words Treatment
    - Spelling Correction
    - Stop-word removal
    - Handling Emoji
    - Tokenization

  - Demonstrates how raw text is prepared before applying NLP models.

---

### 2. Vectorization Techniques
- **`Vectorization_Techniques.ipynb`**
  - Explains how text data is converted into numerical form.
  - Includes:
    - One-Hot Encoding
    - Bag-of-Words
    - N-Grams
    - TF-IDF
  - Shows how different vector representations affect text modeling.

---

### 3. Part-of-Speech (POS) Tagging
- **`pos-tagging.ipynb`**
  - Demonstrates Part-of-Speech tagging.
  - words are classified as nouns, verbs, adjectives, etc.
  - Useful for understanding grammatical structure in text.

---

### 4. Word Embeddings (Word2Vec)
- **`gensim.ipynb`**
  - Uses the Gensim library for Word2Vec.
  - Demonstrates how words are represented as dense vectors.
  - Shows semantic similarity between words.

- **`word2vec game_of_thrones.ipynb`**
  - Applies Word2Vec on a `Game of Thrones` book.
  - Used to analyze word relationships in a real text corpus.

---

### 5. Text Classification
- **`text-classification using machine learning.ipynb`**
  - Implements text classification using traditional machine learning models.
  - Covers the complete pipeline:
    - Preprocessing
    - Vectorization
    - Model training
    - Evaluation

- **`text-classification with word2vec using machine learning.ipynb`**
  - Uses Word2Vec embeddings as features.
  - Compares embedding-based classification with traditional approaches.

---

### 6. Python Script
- **`preceptron Email spam.py`**
  - A standalone Python script.
  - Implements a basic perceptron-based spam classifier.
  - Focuses on understanding classification logic without notebooks.

### `**etc**`
---

## The repository is intended to serve as:
- a technical reference for fundamental NLP workflows,
- a clear demonstration of algorithmic behavior on textual data,
- and a concise, implementation-focused record of applied NLP methods,
- a foundation for extending experiments toward more advanced models and architectures,
- and a reproducible baseline for comparative analysis and further research.

---

## Tools & Libraries Used
- Python
- Jupyter Notebook
- NLTK
- Spacy
- Gensim
- Scikit-learn

---

Thank you for taking the time to look through this work.
