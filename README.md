
---



# Automated Resume Relevance Check System

🚀 **Resume Relevance Checker MVP**

---

## Problem Statement

At Innomatics Research Labs, resume evaluation is manual, inconsistent, and slow, impacting the placement process. The goal is to automate resume evaluation at scale, generate relevance scores, highlight gaps, and provide actionable feedback to students. This system speeds up shortlisting and aids placement teams by offering consistent, AI-driven resume analysis against job descriptions.

---

## Approach

This MVP uses a hybrid AI approach:

- **Hard Match:** Keyword and skill matching between resumes and job descriptions.
- **Semantic Match:** Embeddings and large language models (LLMs) for contextual understanding.
- Combines scores for an overall relevance rating (0-100).
- Provides verdicts (High/Medium/Low) and missing skills/projects.
- Built with Python, Streamlit (for UI), LangChain, and LLM APIs.
- Fast resume parsing using PyMuPDF and python-docx.
- Results presented in a user-friendly web app dashboard for placement teams.

---

## Installation

### Prerequisites

- Python 3.8 or above
- pip package manager

### Steps

1. Clone the repository:


2. Create and activate a virtual environment:


3. Install dependencies:


4. Run the Streamlit app:


## Usage

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Paste or upload a Job Description (JD).
3. Upload one or more resumes (PDF or DOCX).
4. Click **Evaluate** to get relevance scores, verdicts, and missing skills.
5. View results in an interactive table with detailed feedback per resume.

---

## Tech Stack

- Python (core logic and parsing)
- Streamlit (frontend UI)
- LangChain, LangGraph, LangSmith (LLM orchestration)
- PyMuPDF, python-docx (document parsing)
- Vector similarity (embedding-based semantic matching)

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

---

## Author

SAKSHAM VERMA (Saksham-ai-ux)

---

## License

This project is licensed under the MIT License.

