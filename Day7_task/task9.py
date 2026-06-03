# Task 9: Masking, Broadcasting, and Cosine Similarity

import numpy as np

# ----------------------------------
# Create an Array
# ----------------------------------

scores = np.array([45, 60, 75, 90, 55, 80])

print("Original Array:")
print(scores)

# ----------------------------------
# Boolean Masking
# ----------------------------------

# Select scores greater than or equal to 70
high_scores = scores[scores >= 70]

print("\nScores >= 70:")
print(high_scores)

# ----------------------------------
# Broadcasting
# ----------------------------------

# Add 5 bonus points to every score
updated_scores = scores + 5

print("\nScores After Adding 5 Bonus Points:")
print(updated_scores)

# ----------------------------------
# Cosine Similarity Function
# ----------------------------------

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Computes cosine similarity between two vectors.
    """

    dot_product = np.dot(v1, v2)

    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    similarity = dot_product / (magnitude_v1 * magnitude_v2)

    return similarity


# ----------------------------------
# Test Pair 1
# ----------------------------------

vector_a = np.array([1, 2, 3])
vector_b = np.array([2, 4, 6])

similarity_1 = cosine_similarity(vector_a, vector_b)

print("\nCosine Similarity (Pair 1):")
print(similarity_1)

# ----------------------------------
# Test Pair 2
# ----------------------------------

vector_c = np.array([1, 0, 0])
vector_d = np.array([0, 1, 0])

similarity_2 = cosine_similarity(vector_c, vector_d)

print("\nCosine Similarity (Pair 2):")
print(similarity_2)