import streamlit as st
from llm_utils import improve_resume

st.set_page_config(page_title="AI Resume Improver", layout="wide")

st.title("🧠 AI Resume Improver")
st.write("Paste your resume (and optionally a job description) to get targeted improvements.")

resume_text = st.text_area(
    "Paste your resume text here:",
    height=250,
    placeholder="Copy–paste your resume from Word/LinkedIn…",
)

job_description = st.text_area(
    "Optional: Paste the job description here:",
    height=200,
    placeholder="Paste the JD if you want tailored suggestions…",
)

if st.button("✨ Improve My Resume", type="primary"):
    if not resume_text.strip():
        st.warning("Please paste your resume first.")
    else:
        with st.spinner("Generating improvements..."):
            result = improve_resume(resume_text, job_description or None)
        st.markdown("### ✅ Suggestions & Improved Version")
        st.markdown(result)
