"""
Prompt templates for resume tailoring Streamlit app using LangChain.
"""

from langchain_core.prompts import PromptTemplate

job_match_prompt = PromptTemplate.from_template("""You are an assistant helping determine if a job listing is relevant to a candidate's skill set.

Candidate's Skills:
{skills}

Job Description:
{job_post}

Your task:
- Determine if the job is a good match for the candidate's skills.
- A match does not require exact keyword overlap. It can include:
    • Related tools, frameworks, or languages
    • Similar job responsibilities
    • Overlapping domains (e.g., "data analysis" and "data science")
- Prioritize relevance and practical applicability over exact term matching.

Only reply with one of the following:
- "True" — if the job is related or a close match
- "False" — if the job is unrelated or significantly different

Respond with only **"True"** or **"False"**.
""")

resume_prompt = PromptTemplate.from_template("""You are a professional resume writer.

Your task is to create a tailored version of a candidate's resume that aligns closely with a given job description. Emphasize relevant skills, experiences, and achievements while removing or minimizing unrelated details.

Job Description:
{job_post}

Candidate's Current Resume:
{cv_data}

Guidelines:
- Prioritize aligning the resume with the job’s required skills and responsibilities.
- Highlight technologies, tools, or experience explicitly mentioned in the job post.
- Remove or minimize experience that is irrelevant to the job.
- Keep formatting clear and professional, using sections like "Summary", "Skills", "Experience", and "Education".
- Use plain text output only.

Return the final tailored resume in clean, structured plain text.
""")

approval_prompt = PromptTemplate.from_template("""You are an expert career advisor.

Please review the following tailored resume in the context of the given job description.
Determine if this resume is ready to be submitted. If it aligns well with the job and looks professional, respond with "True". If it needs improvements, respond with "False".

Job Description:
{job_post}

Tailored Resume:
{tailored_resume}

Respond with only "True" or "False".
""")
