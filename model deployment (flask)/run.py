import numpy as np
import tensorflow as tf
import requests

# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('recommendation_rankingbased(dim32).h5')

# Test
test_ratings = {}
test_mountain_ids = np.arange(1, 213)
# print(test_mountain_ids)
for mountain_id in test_mountain_ids:
    test_ratings[mountain_id] = new_model({
        "user_id": np.array([5]),
        "mountain_id": np.array([mountain_id])
    })

# print(test_ratings.items())
# for i in test_ratings.items():
#     print(i[1])
#     break
# print("Ratings:")
# for title, score in sorted(test_ratings.items(), key=lambda x: x[1], reverse=True)[:10]:
#     print(f"{title}: {score}")
#     print(f"{title}")
result = [title for title, score in sorted(test_ratings.items(), key=lambda x: x[1], reverse=True)[:10]]

mountain_name = []
for i in result:
  r = requests.get('https://firestore.googleapis.com/v1beta1/projects/mountain-travel-bangkit/databases/(default)/documents/mountain/' + str(i))
  s = r.json()
  for k,v in s['fields']['Nama'].items():
      mountain_name.append(v)

print(mountain_name)
print(result)
