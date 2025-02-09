from src.scraper import get_repos, get_readme_url, scrape_readme
from src.summarizer import process_github_projects
import streamlit as st


# GitHub token (optional)
TOKEN = ""


def main():
    st.title("GitHub Project Summarizer")
    # Replace with the GitHub username you want to scrape
    username = st.text_input("Enter GitHub username")
    #username = "Santilopezc"
    
    # Get the list of repositories
    repos = get_repos(username, TOKEN)
    readme_dict = {}
    
    for repo in repos:
        repo_name = repo["name"]
        st.write(f"Scraping README for repository: {repo_name}")
        
        # Get the README URL
        readme_url = get_readme_url(repo_name, username, TOKEN)
        
        if readme_url:
            # Scrape the README content
            readme_content = scrape_readme(readme_url)
            if readme_content:
                readme_dict[repo_name] = readme_content
                #print(f"README content for {repo_name}:\n{readme_content}\n")
            else:
                st.write(f"No README content found for {repo_name}\n")
        else:
            st.write(f"No README found for {repo_name}\n")
    projects_summary = process_github_projects(readme_dict, "markdown")
    st.markdown(projects_summary)
    #print(projects_summary)

if __name__ == "__main__":
    main()