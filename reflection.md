# Reflection

- **High-Energy Pop vs. Chill Lofi:** The High-Energy Pop profile should rank upbeat songs with happy moods and stronger energy higher, while Chill Lofi should move toward calmer songs with more acoustic sound. That makes sense because these profiles are asking for very different listening experiences.

- **High-Energy Pop vs. Deep Intense Rock:** These profiles may share some high-energy songs, but they should not always return the same results. Pop should lean more cheerful and catchy, while rock should lean more intense and aggressive. If a song like “Gym Hero” shows up for both, it is probably because the energy score is strong enough to outweigh the style difference.

- **Chill Lofi vs. Deep Intense Rock:** These two should look very different. Chill Lofi should prefer soft, relaxed songs, while Deep Intense Rock should prefer louder and more powerful songs. If the outputs are far apart, that shows the recommender is responding correctly to the user profile.

- **Conflicting profiles:** When a profile asks for things that do not fit together well, like high energy but sad mood, the recommendations can look mixed. That happens because the system tries to satisfy every preference, but one strong feature may still push a song to the top. This helps explain why a song can keep showing up even when it does not seem perfect at first glance.

- **Extreme vs. middle profiles:** Extreme profiles usually produce clearer results because they strongly point the recommender in one direction. The middle profile gives the system less to work with, so more songs can seem equally good. That makes the recommendations less specific.

Overall, the project showed that recommenders turn user preferences into scores, and the output changes when those preferences change. It also showed that if one feature is too strong, like genre or energy, the recommender can keep favoring songs like “Gym Hero” even when a user asked for something more like “Happy Pop.”