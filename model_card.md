# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0** 

---

## 2. Intended Use  
This recommender suggests a small set of songs from a fixed catalog based on a user's preferred genre, mood, energy level, and acoustic preference. It is designed for classroom exploration and testing, not for real-world music recommendation.

It assumes user taste can be represented with a few simple preferences and that similar songs can be ranked using a weighted score.


---

## 3. How the Model Works  

The model compares each song to a user profile using genre, mood, energy, and acousticness. A song gets points when its genre matches the user’s favorite genre, when its mood matches, when its energy is close to the user’s target energy, and when its acousticness fits the user’s preference.

The final recommendation score is a weighted sum of those feature matches. I changed the starter logic by increasing the importance of energy and reducing the importance of genre, so energy differences have more influence on the ranking.


---

## 4. Data  

The model uses a small CSV catalog of songs with attributes like genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is limited, so only a few music styles and moods are represented.

Because the catalog is small, some preferences may be underrepresented. That means the recommender may repeat similar songs or miss more diverse matches.


---

## 5. Strengths  

The system works well when a user has clear preferences and those preferences match features in the catalog. It can give reasonable results for users who care about genre, mood, and energy in a simple way.

It also explains recommendations clearly, which makes it easy to understand why a song was ranked highly.
---

## 6. Limitations and Bias 

The model does not consider lyrics, artist familiarity, listening history, or context like time of day. It also may favor users whose tastes match the most common patterns in the dataset.

If genre is weighted too strongly, the recommender can become repetitive and ignore good matches in other categories. Users with unusual or conflicting tastes may get less useful recommendations.

---

## 7. Evaluation  

I tested the recommender with several user profiles, including normal profiles and adversarial edge cases. I looked at the top-ranked songs and checked whether the explanations matched the scores.

I also changed the feature weights to see whether rankings changed in meaningful ways. This helped show whether the system was sensitive to energy and genre in a balanced way.

---

## 8. Future Work  

The model could be improved by adding more features, such as tempo, valence, or danceability. It would also help to use a larger and more diverse song catalog.

A better version could include diversity logic so the top results are not too similar to each other. It could also provide stronger explanations and learn from user feedback over time.

---

## 9. Personal Reflection  

I learned that recommender systems turn data into predictions by converting user preferences and item features into scores. I also learned that small changes in weights can have a big effect on ranking.

One interesting result was how easily the recommender could over-focus on one feature, especially with a small dataset. This changed the way I think about music apps, because even simple recommendation systems can shape what users see in a strong and biased way.
