# generate.py

import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


def generate_text(model, tokenizer, input_text, next_words, max_sequence_len):
    r"""
    Generate text using the trained LSTM model.

    Theory:
    - The model generates text by predicting the next word based on the previous words in the sequence.
    - The predicted word is then appended to the input_text, and the process repeats.

    Mathematical Notation:
    - Given a input_text \( w_1, w_2, \dots, w_t \), the model predicts \( w_{t+1} \) using the probability distribution \( P(w_{t+1} | w_1, w_2, \dots, w_t) \).

    Args:
        model: The trained LSTM model.
        tokenizer: The tokenizer used for preprocessing.
        input_text (str): The initial text to start the generation.
        next_words (int): Number of words to generate.
        max_sequence_len (int): The maximum sequence length for padding.

    Returns:
        str: The generated output_text.
    """
    output_text = ""
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([input_text])[0]
        token_list = pad_sequences(
            [token_list], maxlen=max_sequence_len - 1, padding="pre"
        )
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=-1)
        output_word = tokenizer.index_word[predicted_word_index[0]]
        output_text += " " + output_word
    return output_text
