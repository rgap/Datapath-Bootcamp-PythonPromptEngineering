# tokenization.py

import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


def tokenize_corpus(corpus):
    """
    Tokenize the corpus and return the tokenizer, input sequences, and the maximum sequence length.

    Theory:
    - Tokenization is the process of converting text into a sequence of tokens (words or subwords).
    - Each word is assigned a unique integer index, creating a sequence of integers.
    - Let the corpus be represented as a sequence of words \( w_1, w_2, \dots, w_T \).
    - The tokenizer assigns each word \( w_i \) an integer \( x_i \), creating a sequence of indices \( x_1, x_2, \dots, x_T \).

    Args:
        corpus (str): The text corpus to tokenize.

    Returns:
        tokenizer: The Keras Tokenizer object.
        input_sequences: A numpy array of padded sequences.
        max_sequence_len: The maximum sequence length for padding.
    """
    # Initialize the tokenizer
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([corpus])
    total_words = len(tokenizer.word_index) + 1  # +1 for padding token

    # Convert text to sequences of integers
    input_sequences = []
    for line in corpus.split("."):
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[: i + 1]
            input_sequences.append(n_gram_sequence)

    # Pad sequences to ensure uniform length
    max_sequence_len = max([len(seq) for seq in input_sequences])
    input_sequences = np.array(
        pad_sequences(input_sequences, maxlen=max_sequence_len, padding="pre")
    )

    return tokenizer, input_sequences, max_sequence_len
