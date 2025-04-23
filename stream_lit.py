
import streamlit as st
import os
from langchain.chat_models import init_chat_model
from prompts import job_match_prompt, resume_prompt, approval_prompt

# Set up API key input
st.title("AI-Powered Resume Tailor")
api_key = st.text_input("Enter your GROQ API Key", type="password")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

# Initialize model
model = init_chat_model("llama3-70b-8192", model_provider="groq")

# User inputs
job_post = st.text_area("Paste Job Description")
cv_data = st.text_area("Paste Your CV or LinkedIn Profile Content")
skills = st.text_input("Enter Your Skills (comma-separated)")

# Button to trigger processing
if st.button("Generate Tailored Resume"):
    if not api_key or not job_post or not cv_data or not skills:
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Evaluating job relevance..."):
            relevance_chain = job_match_prompt | model
            relevance_result = relevance_chain.invoke({"job_post": job_post, "skills": skills})
            is_relevant = "true" in str(relevance_result).lower()

        if not is_relevant:
            st.error("The job doesn't appear to match your skills.")
        else:
            with st.spinner("Generating tailored resume..."):
                resume_chain = resume_prompt | model
                resume_result = resume_chain.invoke({"job_post": job_post, "cv_data": cv_data})
                tailored_resume = resume_result.content.strip()

            st.subheader("Tailored Resume")
            st.text_area("Resume Output", tailored_resume, height=300)

            with st.spinner("Checking resume quality..."):
                approval_chain = approval_prompt | model
                approval_result = approval_chain.invoke({"job_post": job_post, "tailored_resume": tailored_resume})
                is_approved = "true" in str(approval_result).lower()

            if is_approved:
                st.success("Resume is ready to submit!")
            else:
                st.warning("Resume may need improvements before submission.")
