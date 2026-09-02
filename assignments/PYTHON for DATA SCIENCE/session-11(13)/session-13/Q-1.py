#Write a Python function called get_song_duration_per_minute that divides the total duration of a Spotify playlist (in minutes) by the number of songs, and handles the case where the number of songs is zero using try, except, and finally blocks.

def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        print(total_duration / number_of_songs)
    except ZeroDivisionError:
        print("Number of songs cannot be zero.")
    finally:
        print("Calculation completed.")

get_song_duration_per_minute(300, 10)
get_song_duration_per_minute(300, 0)