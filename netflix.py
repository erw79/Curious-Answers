def recommend_tv_show():
    print("Welcome to the TV Show Recommender!")
    print("Answer the following questions to get a recommendation.")

    # Question 1
    genre = input("What genre do you prefer? (Comedy, Drama, Sci-Fi, Mystery): ").strip().lower()

    # Question 2
    setting = input("Do you prefer modern settings, historical settings, or futuristic settings? ").strip().lower()

    # Question 3
    mood = input("What kind of mood are you in? (Light-hearted, Thought-provoking, Intense): ").strip().lower()

    # Recommendations
    if genre == "comedy" and mood == "light-hearted":
        recommendation = "Brooklyn Nine-Nine"
    elif genre == "drama" and setting == "historical":
        recommendation = "Downton Abbey"
    elif genre == "sci-fi" and setting == "futuristic":
        recommendation = "The Expanse"
    elif genre == "mystery" and mood == "intense":
        recommendation = "True Detective"
    else:
        recommendation = "Stranger Things"  # Default recommendation

    print(f"\nBased on your answers, you might enjoy watching: {recommendation}!")

# Run the program
recommend_tv_show()