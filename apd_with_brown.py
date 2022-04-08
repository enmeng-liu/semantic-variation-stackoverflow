import os, pickle, json
import numpy as np
from scipy.spatial import distance
import torch

def apd(array1, array2, metric='cosine'):
    return np.nanmean(distance.cdist(array1, array2, metric='cosine'))

corpus_path = "/data/StackOverflow/Communityposts/data/annual/"
year = 2012

# Get common words with brown
with open(os.path.join(corpus_path, 'frequency', 'common-words-brown.pkl'), 'rb') as f:
    common_words_brown = pickle.load(f)

# Load brown embeddings
with open(os.path.join(corpus_path, 'embeddings','common-words-embeddings-brown-base.pkl'), 'rb') as f:
    w2u_brown = pickle.load(f)

# Load SO embeddings
word2use_so = torch.load(os.path.join(corpus_path, 'embeddings','common-words-embeddings-{}-truncated-base-brown.pt'.format(year)))

# Calculate apd
word2apd_so_brown = {}
for word in common_words_brown:
    try:
        word2apd_so_brown[word] = apd(np.array(word2use_so[word]), np.array(w2u_brown[word]))
    except ValueError:
        print(word, 'not in so')
    except KeyError:
        print(word, 'not in w2u_brown')

# Sort apd
word2apd_so_brown_sorted = {k: v for k, v in sorted(word2apd_so_brown.items(), key=lambda x: -x[1])}

# Save sorted apd
with open(os.path.join(corpus_path, 'apd', 'apd-{}-brown-base.pkl'.format(year)), 'wb') as f:
    pickle.dump(word2apd_so_brown_sorted, f)
with open(os.path.join(corpus_path, 'apd', 'apd-{}-brown-base.json'.format(year)), 'w') as f:
    json.dump(word2apd_so_brown_sorted, f)

print(year, "completed.")