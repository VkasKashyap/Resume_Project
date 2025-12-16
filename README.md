# 📄 AI Resume Screener & Optimizer

**A Smart ATS (Applicant Tracking System) tool that helps job seekers improve their resume chances.**

## 🚀 Live Demo
👉 **[Click here to use the App](https://resumeproject-hnhbbqwkoyg5xgz43skwvh.streamlit.app/)**

---

## 🧐 Problem Statement
Job seekers often get rejected by automated ATS systems because their resumes miss specific keywords found in the job description. It is difficult to manually check every job post against a resume.

## 💡 The Solution
I built an AI-powered tool that:
1.  **Extracts text** from a PDF resume.
2.  **Compares it** against a Job Description using NLP.
3.  **Calculates a Match Score %** (0-100).
4.  **Identifies Missing Keywords** that the user should add to increase their chances.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend:** Streamlit
* **NLP Logic:** TF-IDF Vectorizer (scikit-learn)
* **Similarity Check:** Cosine Similarity
* **PDF Processing:** PyPDF2

---

## ⚙️ How to Run Locally
If you want to run this project on your own computer:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/VkasKashyap/Resume_Project.git](https://github.com/VkasKashyap/Resume_Project.git)
    cd Resume_Project
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 How It Works (Technical Details)
1.  **Text Extraction:** The app uses `PyPDF2` to scrape text from the uploaded PDF.
2.  **Vectorization:** It uses `TfidfVectorizer` to convert both the Resume and Job Description into numerical vectors.
3.  **Cosine Similarity:** It calculates the angle between the two vectors. A smaller angle means a higher match.
4.  **Keyword Extraction:** It converts texts into "Sets" and finds the difference (`Job_Description_Set - Resume_Set`) to find missing words.