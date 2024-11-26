import pandas as pd

# Sample data for simplicity - fill this with actual animals and questions
data = {
    "Animal": ["Dog", "Cat", "Elephant", "Snake", "Eagle"],
    "Has Fur": [True, True, False, False, False],
    "Can Fly": [False, False, False, False, True],
    "Is Mammal": [True, True, True, False, False],
    "Lays Eggs": [False, False, False, True, True],
    # Add more columns/questions as needed
}

# Create DataFrame with sample data
df = pd.DataFrame(data) 
#Will have the df already. 

#will need to abstract questions into list from column names. 
# List of questions for user, corresponding to DataFrame columns (excluding 'Animal')
questions = [
    "Has Fur", 
    "Can Fly", 
    "Is Mammal", 
    "Lays Eggs",
    # Add more questions here as needed
]

# Initialize possibilities with all animals
possibilities = df

print("Welcome to the 20 Questions Game! Let's find out which animal you're thinking of.")

# Loop through each question to filter possibilities
for question in questions:
    answer = input(f"Does the animal you're thinking of {question.lower()}? (yes/no): ").strip().lower()

    # Filter based on user's answer
    if answer == 'yes':
        possibilities = possibilities[possibilities[question] == True]
    elif answer == 'no':
        possibilities = possibilities[possibilities[question] == False]
    else:
        print("Please answer with 'yes' or 'no'.")
        continue  # Re-ask the same question if input is invalid

    # Check if we have narrowed down to one possibility
    if len(possibilities) == 1:
        print(f"The animal you're thinking of is: {possibilities.iloc[0]['Animal']}")
        break
    elif len(possibilities) == 0:
        print("No matching animals found. Are you sure about your answers?")
        break

# If we run out of questions but still have possibilities, list remaining options
if len(possibilities) > 1:
    print("I couldn't narrow it down to just one animal. Here are the possibilities:")
    print(possibilities['Animal'].tolist())
