import random

# Probabilistic Transition Table (First-Order Markov Model)
# In a first-order Markov model, the probability of transitioning to the next state (word) depends only on the current state (word).
# The transition probabilities are denoted as P(w_{i+1} | w_i), where w_i is the current word and w_{i+1} is the next word.
# The sum of probabilities for all possible transitions from a given word must equal 1.

# Transition Probability Table:
# -----------------------------------------------------------------------
# Current Word (w_i)   | Next Word (w_{i+1})       | P(w_{i+1} | w_i)
# ---------------------|--------------------------|-------------------
# once                 | upon                      | P(upon | once) = 1.0
# upon                 | a                         | P(a | upon) = 1.0
# a                    | time, land                | P(time | a) = 0.5, P(land | a) = 0.5
# time                 | in, there                 | P(in | time) = 0.6, P(there | time) = 0.4
# in                   | a, the                    | P(a | in) = 0.7, P(the | in) = 0.3
# land                 | far                       | P(far | land) = 1.0
# far                  | far                       | P(far | far) = 1.0
# there                | was                       | P(was | there) = 1.0
# was                  | a                         | P(a | was) = 1.0
# little               | girl                      | P(girl | little) = 1.0
# girl                 | found                     | P(found | girl) = 1.0
# found                | a                         | P(a | found) = 1.0
# magic                | ring                      | P(ring | magic) = 1.0
# ring                 | [end]                     | P([end] | ring) = 1.0

transition_table = {
    "once": {"upon": 1.0},  # P(upon | once) = 1.0
    "upon": {"a": 1.0},  # P(a | upon) = 1.0
    "a": {"time": 0.5, "land": 0.5},  # P(time | a) = 0.5, P(land | a) = 0.5
    "time": {"in": 0.6, "there": 0.4},  # P(in | time) = 0.6, P(there | time) = 0.4
    "in": {"a": 0.7, "the": 0.3},  # P(a | in) = 0.7, P(the | in) = 0.3
    "land": {"far": 1.0},  # P(far | land) = 1.0
    "far": {"far": 1.0},  # P(far | far) = 1.0
    "there": {"was": 1.0},  # P(was | there) = 1.0
    "was": {"a": 1.0},  # P(a | was) = 1.0
    "little": {"girl": 1.0},  # P(girl | little) = 1.0
    "girl": {"found": 1.0},  # P(found | girl) = 1.0
    "found": {"a": 1.0},  # P(a | found) = 1.0
    "magic": {"ring": 1.0},  # P(ring | magic) = 1.0
    "ring": {"[end]": 1.0},  # P([end] | ring) = 1.0
}


def generate_text_probabilistic(input_text, max_words=20):

    # Convert the input text to lowercase and remove leading/trailing whitespaces
    input_text = input_text.lower().strip()

    # Use the last word of the input_text to start the text generation
    start_word = input_text.split()[-1]

    current_word = start_word
    sentence = [current_word]

    while len(sentence) < max_words:
        next_word_probs = transition_table.get(current_word, None)

        if not next_word_probs:
            break

        # Randomly choose the next word based on the probabilities
        next_words = list(next_word_probs.keys())
        probabilities = list(next_word_probs.values())
        next_word = random.choices(next_words, probabilities)[0]

        if next_word == "[end]":
            break

        sentence.append(next_word)
        current_word = next_word

    return " ".join(sentence)


# Define the initial input_text and prepare it
input_text = "Once upon a time"

# Generate a sentence using the Probabilistic Markov Model
output_text = generate_text_probabilistic(input_text)

# Print the generated text
response = input_text + " " + output_text
print(response)
