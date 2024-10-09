import random

# Initialize counters for the number of times "big" and "small" occur
big_count = 0
small_count = 0

# Store previous events to track sequences
event_history = []

# Function to predict the next event based on probabilities
def predict_next_event():
    global big_count, small_count
    if big_count + small_count == 0:
        # If no events entered yet, randomly choose
        return random.choice(["big", "small"])
    else:
        # Calculate probabilities
        prob_big = big_count / (big_count + small_count)
        prob_small = small_count / (big_count + small_count)
        # Predict based on higher probability
        return "big" if prob_big > prob_small else "small"

# Run the event prediction system
while True:
    # Get user input for the current event
    current_event = input("Enter the current event (b/sGIT  or 'q' to quit): ").lower()

    # If user wants to quit
    if current_event == 'q':
        print("Exiting...")
        break

    # If input is valid
    if current_event in ["b", "s"]:
        # Add to event history
        event_history.append(current_event)

        # Update counters
        if current_event == "big":
            big_count += 1
        else:
            small_count += 1

        # Predict the next event
        predicted_event = predict_next_event()
        print(f"Predicted next event: {predicted_event}")

    else:
        print("Invalid input. Please enter 'big' or 'small'.")
