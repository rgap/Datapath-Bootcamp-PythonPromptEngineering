# This example demonstrates a basic interaction with a simulated text completion model.

# Define a simple text input
prompt = "Complete this sentence: Once upon a time"


# Simulated text completion response
def simulate_text_completion(prompt):
    # Check if the prompt starts with "Complete this sentence:"
    if prompt.lower().startswith("complete this sentence:"):
        # Extract the actual sentence after the prefix
        sentence = prompt[len("Complete this sentence:") :].strip()
        # Provide the simulated completion
        if sentence.lower() == "once upon a time":
            return (
                sentence
                + ", in a land far, far away, there was a small village surrounded by lush forests."
            )
        else:
            return sentence + " [Completion not available]."
    else:
        return "[Invalid prompt]"


# Get the completion from the simulated model
response = simulate_text_completion(prompt)

# Print the final response
print(
    response
)  # Expected output: "Once upon a time, in a land far, far away, there was a small village surrounded by lush forests."
