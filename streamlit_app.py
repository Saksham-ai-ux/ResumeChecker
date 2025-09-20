import streamlit as st
import pandas as pd
from app.utils_parser import extract_text_from_file, parse_jd_simple
from app.scorer import hard_match_score, semantic_score, combined_score, verdict

# Set page config with title and icon
st.set_page_config(page_title="Resume Relevance Checker", page_icon=":rocket:", layout="wide")

# Sidebar info
with st.sidebar:
    st.markdown("### Powered by GenAI")
    st.markdown("_Made for Innomatics Research Labs_")
    st.divider()
    st.markdown("**Contact:** classic.saksham@gmail.com")

# Instructions expander
with st.expander("ℹ️ How to use this app"):
    st.markdown("""
    1. Paste or upload the **Job Description (JD)**.
    2. Upload multiple resumes (PDF/DOCX).
    3. Click **Evaluate** to see scores and verdicts.
    """)

# Centered title
st.markdown("<h1 style='text-align: center;'>🚀 Resume Relevance Checker MVP</h1>", unsafe_allow_html=True)

# JD paste/upload area
jd_text = st.text_area("Paste Job Description (JD)", height=150)
jd_file = st.file_uploader("Or upload JD file", type=["pdf", "docx", "txt"])

if jd_file and not jd_text:
    jd_text = extract_text_from_file(jd_file.name, jd_file.read())

if jd_text:
    jd = parse_jd_simple(jd_text)
    st.write("**Role:**", jd["title"])
    st.write("**Must-have:**", jd["must"])
    st.write("**Good-to-have:**", jd["good"])
    
    resumes = st.file_uploader("Upload resumes", type=["pdf", "docx"], accept_multiple_files=True)
    
    if resumes and st.button("Evaluate"):
        rows = []
        with st.spinner("Analyzing resumes..."):
            for r in resumes:
                txt = extract_text_from_file(r.name, r.read())
                hard, missing = hard_match_score(jd["must"], txt)
                soft = semantic_score(jd_text, txt)
                score = combined_score(hard, soft)
                rows.append({
                    "Resume": r.name,
                    "Score": score,
                    "Verdict": verdict(score),
                    "Missing": ", ".join(missing)
                })
        st.success("Analysis complete!")
        
        # Sort dataframe by Score descending and display nicely
        df = pd.DataFrame(rows).sort_values("Score", ascending=False)
        st.dataframe(df, use_container_width=True)
        
        # Show summary with colored verdict and relevance progress bars
        for index, row in df.iterrows():
            score = row["Score"]
            verdict_text = row["Verdict"]
            missing_text = row["Missing"]
            
            st.markdown(f"### 📄 {row['Resume']}")
            st.progress(int(score))
            st.markdown(f"**Verdict:** :star2: {verdict_text}")
            if missing_text:
                st.markdown(f"**Missing Skills/Projects:** {missing_text}")
            st.divider()
