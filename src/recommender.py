from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """_summary_

    Args:
        user_prefs (Dict): _description_
        song (Dict): _description_

    Returns:
        Tuple[float, List[str]]: _description_
    """    
    score = 0.0
    reasons: List[str] = []
    GENRE_WEIGHT = 1.0      # was effectively 2.0, reduced by half
    MOOD_WEIGHT = 1.0       # unchanged
    ENERGY_WEIGHT = 2.0     # doubled from 1.0
    ACOUSTIC_WEIGHT = 1.0   # unchanged

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 1.0 * GENRE_WEIGHT
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0 * MOOD_WEIGHT
        reasons.append("mood match (+1.0)")

    energy_points = 1.0 - abs(song["energy"] - user_prefs["target_energy"])
    score += 1.0 * ENERGY_WEIGHT
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    acoustic_points = song["acousticness"] if user_prefs["likes_acoustic"] else 1 - song["acousticness"]
    score += 1.0 * ACOUSTIC_WEIGHT
    reasons.append(f"acousticness (+{acoustic_points:.2f})")

    return score, reasons

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(asdict(user), asdict(song))[0],
            reverse=True
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        score, reasons = score_song(asdict(user), asdict(song))
        return f"Score: {score:.2f}. Reasons: {', '.join(reasons)}"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        ranked.append((song, score, "; ".join(reasons)))

    return sorted(ranked, key=lambda item: item[1], reverse=True)[:k]
