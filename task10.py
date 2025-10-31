# Define a list of facts
facts = [
    "john_is_cold.",          # john is cold
    "raining.",               # it is raining
    "john_Forgot_His_Raincoat.", # john forgot his raincoat
    "fred_lost_his_car_keys.",  # fred lost his car keys
    "peter_footballer."       # peter plays football
]

# Function to check if a fact is true
def verify_fact(fact):
    # Remove the trailing period
    fact = fact.rstrip(".")

    # Perform some logic to verify the fact
    # This acts as a simple "knowledge base"
    if fact == "john_Forgot_His_Raincoat":
        return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return True
    elif fact == "Cloudy":
        return False  # Assume it's not cloudy
    else:
        # All other facts (like john_is_cold, etc.)
        # are not in our knowledge base, so they are false.
        return False

# Verify each fact from the list against the knowledge base
for fact in facts:
    if verify_fact(fact):
        print(f"{fact} - Yes")
    else:
        print(f"{fact} - No")