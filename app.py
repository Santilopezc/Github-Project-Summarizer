from src.scraper import get_repos, get_readme_url, scrape_readme
from src.summarizer import process_github_projects
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

# GitHub token (optional)
TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

def main():
    st.title("GitHub Project Summarizer")
    # Replace with the GitHub username you want to scrape
    username = st.text_input("Enter GitHub username")
    #username = "Santilopezc"
    
    # Get the list of repositories
    repos = get_repos(username, TOKEN)
    readme_dict = {}
    if repos:
        st.write(f"Found {len(repos)} repositories.")
        # Initialize progress bar and status text
        progress_bar = st.progress(0)
        status_text = st.empty()
        total_repos = len(repos)
        
        for i, repo in enumerate(repos):
            repo_name = repo["name"]
            
            # Update progress bar and status text
            progress = (i + 1) / total_repos
            progress_bar.progress(progress)
            status_text.text(f"Processing repository {i + 1} of {total_repos}: {repo_name}")

            readme_url = get_readme_url(repo_name, username, TOKEN)
        
            if readme_url:
                # Scrape the README content
                readme_content = scrape_readme(readme_url)
                if readme_content:
                    readme_dict[repo_name] = readme_content
                else:
                    st.write(f"No README content found for {repo_name}\n")
            else:
                st.write(f"No README found for {repo_name}\n")
        
        # Get the README URL

        projects_summary = process_github_projects(readme_dict)
        if projects_summary:
            st.download_button(
                label="Download Summary",
                data = projects_summary,
                file_name="projects_summary.txt",
            )
    #print(projects_summary)

if __name__ == "__main__":
    main()