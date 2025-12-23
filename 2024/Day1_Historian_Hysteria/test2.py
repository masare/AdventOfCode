import numpy as np

data = np.genfromtxt('input', dtype=np.int32)

# compute the similarity scores
similarity_scores = [d * (data[:,1]==d).sum() for i, d in enumerate(data[:, 0])] 

# compute overall similarity score
overall_similarity_score = np.asarray(similarity_scores, dtype=np.int32).sum()

# output overall similarity score
print(overall_similarity_score)