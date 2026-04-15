"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_profiles = [
        {
            "name": "High-Energy Pop",
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.8,
            "likes_acoustic": False,
        },
        {
            "name": "Chill Lofi",
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.4,
            "likes_acoustic": True,
        },
        {
            "name": "Deep Intense Rock",
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
    ]

    # Adversarial user profiles for recommender testing
    profiles = [
        {
            "name": "conflicting_energy_mood",
            "favorite_genre": "ambient",
            "favorite_mood": "sad",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        {
            "name": "high_conflict_low_energy_happy",
            "favorite_genre": "metal",
            "favorite_mood": "happy",
            "target_energy": 0.1,
            "likes_acoustic": True,
        },
        {
            "name": "all_extremes_maxed",
            "favorite_genre": "classical",
            "favorite_mood": "angry",
            "target_energy": 1.0,
            "likes_acoustic": False,
        },
        {
            "name": "all_extremes_minimized",
            "favorite_genre": "edm",
            "favorite_mood": "excited",
            "target_energy": 0.0,
            "likes_acoustic": True,
        },
        {
            "name": "ambiguous_middle",
            "favorite_genre": "pop",
            "favorite_mood": "neutral",
            "target_energy": 0.5,
            "likes_acoustic": False,
        },
    ]

    for user_prefs in profiles:
        print(f"\n=== {user_prefs['name']} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} — score: {score:.2f}")
            print(f"   reasons: {explanation}")

if __name__ == "__main__":
    main()