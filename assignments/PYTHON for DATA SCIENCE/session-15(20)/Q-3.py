#reate a Movie class with a private attribute _rating (float between 0 and 10). Write getter and setter methods for _rating. The setter should only allow values between 0 and 10; if an invalid value is given, print an error message.<br><br><em><strong>Constraint:</strong> Do not allow direct access to _rating outside the class.</em>


class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = None  # Private attribute initialized
        self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = float(rating)
        else:
            print("Error: Rating must be a number between 0 and 10.")


# Demonstration
if __name__ == "__main__":
    movie = Movie("Inception", 8.8)

    # Getting rating using getter
    print("Movie Rating:", movie.get_rating())

    # Attempting to set a valid rating
    movie.set_rating(9.2)
    print("Updated Rating:", movie.get_rating())

    # Attempting to set an invalid rating
    movie.set_rating(12.5)