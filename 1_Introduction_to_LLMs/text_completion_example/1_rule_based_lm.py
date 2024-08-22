# This example demonstrates a basic interaction with a simulated text completion model.

# Define a simple text input
input_text = "Once upon a time"


# Simulated text completion response
def simulate_text_completion(text):
    if text.lower().strip() == "once upon a time":
        return "in a land far, far away, there was a small village surrounded by lush forests."
    else:
        return "[Completion not available]."


# Get the completion from the simulated model
output_text = simulate_text_completion(input_text)

# Print the completion
print(
    "output_text:\n", output_text
)  # Expected output: "Once upon a time in a land far, far away, there was a small village surrounded by lush forests."

print()

# Print the full text
completed_text = input_text + " " + output_text
print(
    "full_text:\n", completed_text
)  # Expected output: "Once upon a time in a land far, far away, there was a small village surrounded by lush forests."
