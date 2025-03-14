# AI Resume Screening & Candidate Ranking System

## 📌 About the Project
This project is an **AI-powered resume screening system** that helps recruiters shortlist candidates based on job role requirements. The system allows users to **select an engineering profession**, fetches predefined qualifications, and ranks resumes based on their relevance.

## ✨ Features
- **Engineering Role Selection** – Choose from Software Engineer, Data Scientist, or Mechanical Engineer.
- **Predefined Qualifications** – Avoids slow API calls by using in-built qualification requirements.
- **Resume Parsing** – Supports **PDF and DOCX** formats for text extraction.
- **AI-Based Ranking** – Uses **TF-IDF Vectorization & Cosine Similarity** to compare resumes against job descriptions.
- **Percentage Match Score** – Shows how well each resume fits the job role.
- **CSV Export** – Download ranked resumes for easy recruitment decisions.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend Processing:** Python
- **Libraries Used:**
  - `streamlit`
  - `pdfplumber`
  - `python-docx`
  - `scikit-learn`
  - `pandas`

## 🚀 How to Run Locally
### Prerequisites
Ensure you have **Python 3.x** installed. Then, install the required dependencies:
```bash
pip install streamlit pdfplumber python-docx pandas scikit-learn
```

### Steps to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/KarthickRaghul/Resume-Screener.git
   cd Resume-Screener
   ```
2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```
3. **Open the app in your browser** (default: http://localhost:8501)

## 📷 Screenshots
### 1️⃣ Select a Profession
![Profession Selection](docs/profession_selection.png)

### 2️⃣ Upload Resumes
![Resume Upload](docs/resume_upload.png)

### 3️⃣ Ranked Results
![Ranked Results](docs/ranked_results.png)

## 🔥 Future Enhancements
- Add more job roles and industries.
- Implement **AI-driven skill extraction**.
- Enable real-time industry trends analysis.

## 📜 License
This project is **open-source** under the MIT License.

## 🤝 Contributing
Feel free to **fork the repo**, create a new branch, and submit a PR if you have improvements!

## 📧 Contact
For queries, reach out to **[Your Email]** or visit [Your GitHub](https://github.com/KarthickRaghul).

---
### 🌟 Don't forget to ⭐ the repository if you find it useful!

