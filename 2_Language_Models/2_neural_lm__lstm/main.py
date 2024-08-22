# main.py

import tensorflow as tf  # Import TensorFlow
from generate import generate_text
from model import create_lstm_model
from tokenization import tokenize_corpus
from training import train_lstm_model

# Sample corpus for training
corpus = """Once upon a time in a land far far away there was a little girl who found a magic ring.
The ring had the power to grant any wish. She wished for a peaceful and happy life."""

# Step 1: Tokenize the corpus
tokenizer, input_sequences, max_sequence_len = tokenize_corpus(corpus)

# Step 2: Prepare the input and output for training
X = input_sequences[:, :-1]  # Input sequences (X)
y = input_sequences[:, -1]  # Output words (y)
y = tf.keras.utils.to_categorical(
    y, num_classes=len(tokenizer.word_index) + 1
)  # One-hot encode the output

# Step 3: Create the LSTM model
model = create_lstm_model(
    total_words=len(tokenizer.word_index) + 1, max_sequence_len=max_sequence_len
)

# Step 4: Train the LSTM model
train_lstm_model(model, X, y, epochs=100)

# Step 5: Generate new text
input_text = "Once upon a time"
next_words = 20
output_text = generate_text(model, tokenizer, input_text, next_words, max_sequence_len)

response = input_text + output_text
print(response)
