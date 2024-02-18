from django.db import models
from PyPDF2 import PdfReader

from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

# Create your models here.
class Resume:
    def __init__(self, filename):
        # Extract text using the chosen library
        self.text = parse_resume(filename)

    def parse_resume(filename):
    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

    # Extract information using NLP libraries like spaCy or NLTK
    def extract_work_experience(text):
        # ... code to identify sections and extract details ...
        return work_experience_data

    # Similar functions for project_details, education_background, etc.

class Ranking:

    def __init__(self, resume_text, job_description):
        # Extract text using the chosen library
        self.text = calculate_relevance_score(resume_text, job_description)
    
    def calculate_relevance_score(resume_text, job_description):
        vectorizer = TfidfVectorizer()
        resume_vectors = vectorizer.fit_transform([resume_text])
        job_description_vector = vectorizer.transform([job_description])[0]
        tfidf_score = resume_vectors[0].dot(job_description_vector)

        # Sentence embedding using SentenceTransformer
        model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
        resume_embedding = model.encode([resume_text])
        job_description_embedding = model.encode([job_description])[0]
        sentence_embedding_score = cosine_similarity(resume_embedding, job_description_embedding)[0]

        # Combine scores with weights and keyword matching (not shown here)
        return combined_score

class JSON_Format:
    
    def __init__(self, candidate_data):
        # Extract text using the chosen library
        self.text = generate_json_output(candidate_data)

    def generate_json_output(candidate_data):
    json_data = {
        "projects": [],
        "professional_experience": [],
        "college": {
            # ... college information extracted from candidate_data ...
        }
    }

    for project in candidate_data["projects"]:
        json_data["projects"].append({
            "project_title": project["title"],
            "short_description": project["description"],
            # ... other project details ...
        })

    # similar loop for "professional_experience"

    return json.dumps(json_data)