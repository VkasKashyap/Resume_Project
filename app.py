import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# 1. FUNCTION: Extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# 2. FUNCTION: The AI Math (Compare Resume vs Job Description)
def calculate_similarity(resume_text, job_description):
    content = [resume_text, job_description]
    cv = TfidfVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix[0][1] * 100

# 3. NEW FUNCTION: Find Missing Keywords (The "Smart" Part)
def find_missing_keywords(resume_text, job_description):
    # Clean up text (remove special characters, make lowercase)
    def clean_text(text):
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return set(text.lower().split())

    resume_words = clean_text(resume_text)
    job_words = clean_text(job_description)

    # DSA Concept: Set Difference (Words in Job BUT NOT in Resume)
    missing = job_words - resume_words
    
    # Remove common boring words (stopwords) so we only see important skills
    boring_words = {"the", "and", "is", "in", "to", "for", "of", "a", "with", "highly", "motivated", "seeking", "skilled", "ideal", "candidate", "ability", "experience", "years", "working", "knowledge", "strong", "team", "environment"}
    
    # Filter out boring words
    important_missing = [word for word in missing if word not in boring_words]
    
    return list(important_missing)

# --- THE WEBSITE UI ---
st.set_page_config(page_title="AI Resume Screener", page_icon="📄")
st.title("📄 AI Resume Screener & Optimizer")
st.write("Upload your resume to see what keywords you are missing!")

# Input 1: Job Description
job_description = st.text_area("1. Paste the Job Description here:")

# Input 2: Resume Upload
uploaded_file = st.file_uploader("2. Upload your Resume (PDF)", type=["pdf"])

# The Button
if st.button("Analyze Resume"):
    if uploaded_file and job_description:
        # Step A: Extract Text
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Step B: Calculate Score
        score = calculate_similarity(resume_text, job_description)
        
        # Step C: Find Missing Keywords
        missing_keywords = find_missing_keywords(resume_text, job_description)
        
        # --- DISPLAY RESULTS ---
        st.divider() # distinct line
        
        # 1. The Score
        st.subheader("Match Score:")
        if score > 75:
            st.success(f"✅ {round(score, 2)}% - Excellent Match!")
        elif score > 50:
            st.warning(f"⚠️ {round(score, 2)}% - Good, but needs work.")
        else:
            st.error(f"❌ {round(score, 2)}% - Low Match.")

        # 2. The Feedback (Missing Keywords)
        st.subheader("Missing Keywords:")
        if missing_keywords:
            st.write("Your resume is missing these important words from the job description:")
            # Show keywords as red tags
            st.write(missing_keywords[:15]) # Show top 15 missing words
        else:
            st.balloons()
            st.write("Amazing! You have all the keywords!")
            
    else:
        st.info("Please upload a resume and paste the job description to start.")