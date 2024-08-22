from transformers import GPT2LMHeadModel, GPT2Tokenizer


def complete_text_gpt2(input_text, max_length=50):
    """
    Generate text completion using GPT-2.

    Theory:
    - GPT-2 is based on the Transformer architecture, which uses self-attention mechanisms to process input sequences.
    - Unlike LSTMs, which process sequences step-by-step, Transformers can attend to all positions in the sequence simultaneously, capturing long-range dependencies more effectively.
    - GPT-2 is pre-trained on large text corpora, making it highly effective for generating human-like text by predicting the next word in a sequence.

    Mathematical Notation:
    - Let the input sequence be \( \mathbf{X} = [x_1, x_2, \dots, x_t] \), where \( x_i \) represents a word in the sequence.
    - The model's goal is to maximize the probability \( P(x_{t+1} | x_1, x_2, \dots, x_t) \), which represents the likelihood of the next word given the context.
    - GPT-2 achieves this by using self-attention to compute hidden states \( \mathbf{H}_t \) at each position, where:
      \[
      \mathbf{H}_t = \text{SelfAttention}(\mathbf{X}) = \text{softmax}\left(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d_k}}\right) \mathbf{V}
      \]
      Here, \( \mathbf{Q} \) (query), \( \mathbf{K} \) (key), and \( \mathbf{V} \) (value) are linear transformations of the input, and \( d_k \) is the dimensionality of the key vectors.
    - The final probability distribution over the vocabulary is given by:
      \[
      P(x_{t+1} | x_1, x_2, \dots, x_t) = \text{softmax}(\mathbf{W} \mathbf{H}_t + \mathbf{b})
      \]
      where \( \mathbf{W} \) and \( \mathbf{b} \) are learned parameters.

    Args:
        input_text (str): The initial text to start the generation.
        max_length (int): The maximum length of the generated text.

    Returns:
        str: The generated response text.
    """

    # Step 1: Load pre-trained GPT-2 tokenizer and model
    # Theory: The tokenizer converts text into a sequence of integers (tokens) that the model can process.
    # GPT-2 is pre-trained on a large corpus, so it has learned to understand and generate coherent text.
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Step 2: Encode the input_text
    # Theory: The input_text is converted into a tensor of token IDs, which the model uses to generate predictions.
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Step 3: Generate text completion
    # Theory: The model generates the next words in the sequence by iteratively predicting the next word until max_length is reached.
    # The self-attention mechanism allows the model to consider the entire context of the input_text when making predictions.
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,  # Avoid the pad token warning
        attention_mask=None,  # Use the default attention mask if you don't have padding in your input
    )

    # Step 4: Decode the generated text
    # Theory: The output is a sequence of token IDs, which are converted back into human-readable text.
    response = tokenizer.decode(output[0])

    # Step 5: Return the generated response
    return response


# Example usage

# Step 6: Define the input_text for text generation
input_text = "Once upon a time"

# Step 7: Generate a text completion response based on the input_text
response = complete_text_gpt2(input_text, max_length=50)

# Step 8: Print the generated response
print()
print(response)
