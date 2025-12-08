import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env and system env vars
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def improve_resume(resume_text: str, job_description: str | None = None) -> str:
    system_prompt = (
        "You are an expert resume coach for data and tech roles. "
        "Improve the resume to be clear, concise and impact-driven. "
        "Use strong bullet points and quantify results where possible."
    )

    if job_description:
        user_prompt = f"""
Here is my resume:

{resume_text}

Here is the job description:

{job_description}

1. Give 5–10 **specific suggestions** to improve my resume for THIS job.
2. Rewrite my **SUMMARY** section.
3. Rewrite 1–2 key bullet points per role to better match the job.
Respond in Markdown.
"""
    else:
        user_prompt = f"""
Here is my resume:

{resume_text}

1. Give 5–10 **specific suggestions** to improve my resume.
2. Rewrite my **SUMMARY** section.
3. Rewrite 1–2 key bullet points per role to be more impact-focused.
Respond in Markdown.
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=0.4,
    )

    return resp.choices[0].message.content
