movies = {
    "action": ["Avengers", "John Wick", "RRR"],
    "comedy": ["3 Idiots", "Hera Pheri", "Jathi Ratnalu"],
    "horror": ["Conjuring", "Insidious", "Smile"],
    "scifi": ["Interstellar", "Inception", "The Matrix"]
}

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("\nRecommended Movies:")

    for movie in movies[genre]:
        print("-", movie)
else:
    print("Genre not available.")
