# model.py

from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential


def create_lstm_model(total_words, max_sequence_len):
    """
    Create an LSTM model for text generation.

    Theory:
    - The model consists of an Embedding layer, an LSTM layer, and a Dense output layer.
    - The Embedding layer converts integer indices into dense vectors.
    - The LSTM layer processes the sequence of vectors and captures the temporal dependencies.
    - The Dense layer with a softmax activation function outputs a probability distribution over the vocabulary.

    Mathematical Notation:
    - Embedding: \( v_i = \text{Embedding}(x_i) \), where \( v_i \) is the vector representation of word \( w_i \).
    - LSTM: \( h_t = \text{LSTM}(v_t, h_{t-1}) \), where \( h_t \) is the hidden state at time \( t \).
    - Output: \( P(w_t | w_1, w_2, \dots, w_{t-1}) = \text{softmax}(Wh_t + b) \).

    Args:
        total_words (int): The size of the vocabulary.
        max_sequence_len (int): The maximum length of input sequences.

    Returns:
        model: The compiled LSTM model.
    """
    model = Sequential()
    model.add(Embedding(total_words, 10, input_length=max_sequence_len - 1))
    model.add(LSTM(100))
    model.add(Dense(total_words, activation="softmax"))

    # Compile the model with categorical cross-entropy loss and Adam optimizer
    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )

    return model
