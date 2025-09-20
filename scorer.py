from rapidfuzz import fuzz
from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_sim(a, b):
    return float(np.dot(a, b) / (norm(a) * norm(b)))

def hard_match_score(must, resume):
    if not must: return 100.0, []
    resume = resume.lower()
    matched, missing = [], []
    for skill in must:
        if skill.lower() in resume or fuzz.partial_ratio(skill.lower(), resume) > 85:
            matched.append(skill)
        else:
            missing.append(skill)
    return (len(matched)/len(must))*100, missing

def semantic_score(jd, resume):
    a, b = model.encode([jd, resume], convert_to_numpy=True)
    return cosine_sim(a, b)*100

def combined_score(hard, soft):
    return round(0.6*hard + 0.4*soft, 2)

def verdict(score):
    if score >= 75: return "High"
    if score >= 50: return "Medium"
    return "Low"
