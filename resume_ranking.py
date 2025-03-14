import streamlit as st
import pdfplumber
import pandas as pd
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

# Predefined qualifications to avoid API delay
QUALIFICATIONS = {
    "Software Engineer": "Proficiency in Python, Java, or C++. Experience with data structures, algorithms, and system design. Knowledge of databases and web development frameworks.",
    "Data Scientist": "Experience with Python, R, or SQL. Knowledge of machine learning, statistics, and data visualization. Proficiency in TensorFlow, Pandas, and NumPy.",
    "Mechanical Engineer": "Expertise in CAD software, thermodynamics, and materials science. Knowledge of manufacturing processes and mechanical systems design."
}

def download_csv(results):
    output = BytesIO()
    results.to_csv(output, index=False)
    return output.getvalue()

st.title("AI Resume Screening & Candidate Ranking System")

st.header("Select a Profession")
professions = list(QUALIFICATIONS.keys())
selected_profession = st.selectbox("Choose a profession", professions)

if selected_profession:
    st.write(f"Qualifications required for {selected_profession}:")
    qualifications = QUALIFICATIONS[selected_profession]
    st.write(qualifications)

st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF/DOCX files", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files and qualifications:
    st.header("Ranking Resumes")
    resumes = []
    resume_names = []
    
    for file in uploaded_files:
        if file.type == "application/pdf":
            text = extract_text_from_pdf(file)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(file)
        else:
            continue
        resumes.append(text)
        resume_names.append(file.name)

    scores = rank_resumes(qualifications, resumes) * 100  # Convert similarity score to percentage
    results = pd.DataFrame({"Resume": resume_names, "Match Percentage": scores})
    results = results.sort_values(by="Match Percentage", ascending=False)
    st.write(results)
    
    csv = download_csv(results)
    st.download_button("Download Rankings as CSV", csv, "resume_rankings.csv", "text/csv")
