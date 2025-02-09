import openai
from dotenv import load_dotenv
import os

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
    
    for title, readme in readme_dict.items():
        summary = summarize_readme(readme)
        if format == "latex":
            latex_entries.append(format_latex_entry(title, summary))
        else:
            latex_entries.append(format_markdown_entry(title, summary))
    
    return "\n\n".join(latex_entries)