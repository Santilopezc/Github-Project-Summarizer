import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
def summarize_readme(readme_text, model="gpt-4o-mini"):
    """Summarizes a GitHub README file using an LLM."""
    prompt = (
        "Summarize the following GitHub project README in a concise way suitable for a CV:\n\n"
        f"{readme_text}\n\n"
        "The summary should highlight key features, technologies used, and the problem solved."
    )
    
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an expert technical writer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def format_latex_entry(title, summary):
    """Formats the project summary in LaTeX."""
    return f"""
    \subsection*{{{title}}}
    \textbf{{Summary:}} {summary}
    """

def format_markdown_entry(title, summary):
    """Formats the project summary in Markdown."""
    return f"""
    ## {title}
    **Summary:** {summary}
    """

def process_github_projects(readme_dict, format="latex"):
    """Processes multiple GitHub projects and formats them in LaTeX."""
    latex_entries = []
    total_projects = len(readme_dict)
    progress_bar = st.progress(0)  # Initialize progress bar
    status_text = st.empty()  # Placeholder for status text

    for i, (title, readme) in enumerate(readme_dict.items()):
        # Update progress bar and status text
        progress = (i + 1) / total_projects
        progress_bar.progress(progress)
        status_text.text(f"Processing project {i + 1} of {total_projects}: {title}")
        summary = summarize_readme(readme)
        if format == "latex":
            latex_entries.append(format_latex_entry(title, summary))
    
    return "\n\n".join(latex_entries)