# training.py


def train_lstm_model(model, X, y, epochs=100):
    """
    Train the LSTM model on the input data.

    Theory:
    - The model is trained to minimize the categorical cross-entropy loss.
    - The loss function measures the difference between the predicted probability distribution and the actual one-hot encoded output.

    Mathematical Notation:
    - Loss: \( L = -\sum_{i=1}^{N} y_i \log(\hat{y}_i) \), where \( y_i \) is the actual output and \( \hat{y}_i \) is the predicted probability.

    Args:
        model: The LSTM model to train.
        X: The input sequences (training data).
        y: The one-hot encoded output labels.
        epochs (int): Number of training epochs.
    """
    model.fit(X, y, epochs=epochs, verbose=1)
