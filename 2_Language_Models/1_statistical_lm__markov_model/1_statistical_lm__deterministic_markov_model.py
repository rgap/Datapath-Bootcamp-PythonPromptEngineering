import random

# Deterministic Transition Table (First-Order Markov Model)
# In this deterministic first-order Markov model, each word (state) deterministically leads to exactly one next word.
# The transition is denoted as a function f(w_i) = w_{i+1}, where w_i is the current word and w_{i+1} is the next word.
# Since this model is deterministic, f(w_i) always produces the same next word w_{i+1}.

# Transition Function Table:
# ---------------------------------
# Current Word (w_i)   | Next Word (w_{i+1})
# ---------------------|-------------------
# once                 | upon
# upon                 | a
# a                    | time
# time                 | in
# in                   | a
# land                 | far
# far                  | far
# there                | was
# was                  | a
# little               | girl
# girl                 | found
# found                | a
# magic                | ring
# ring                 | [end]

transition_table = {
    "Once": "upon",  # f("Once") = "upon"
    "upon": "a",  # f("upon") = "a"
    "a": "time",  # f("a") = "time"
    "time": "in",  # f("time") = "in"
    "in": "a",  # f("in") = "a"
    "land": "far",  # f("land") = "far"
    "far": "far",  # f("far") = "far" (repeats itself)
    "there": "was",  # f("there") = "was"
    "was": "a",  # f("was") = "a"
    "little": "girl",  # f("little") = "girl"
    "girl": "found",  # f("girl") = "found"
    "found": "a",  # f("found") = "a"
    "magic": "ring",  # f("magic") = "ring"
    "ring": "[end]",  # f("ring") = "[end]" (end of the sentence)
}


def generate_text_deterministic(input_text, max_words=20):

    # Convert the input text to lowercase and remove leading/trailing whitespaces
    input_text = input_text.lower().strip()

    # Use the last word of the input_text to start the text generation
    start_word = input_text.split()[-1]

    current_word = start_word
    sentence = [current_word]

    while len(sentence) < max_words:
        # Deterministically choose the next word
        next_word = transition_table.get(current_word, None)

        # If there's no next word or we hit the end of the sentence, break
        if not next_word or next_word == "[end]":
            break

        sentence.append(next_word)
        current_word = next_word

    return " ".join(sentence)


# Define the initial input_text
input_text = "Once upon a time"

# Generate a sentence using the Deterministic Markov Model
output_text = generate_text_deterministic(input_text)

# Print the generated text
response = input_text + " " + output_text
print(response)
