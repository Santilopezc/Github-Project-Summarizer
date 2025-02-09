import requests
from bs4 import BeautifulSoup

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"

def get_repos(username, token=None):
    """Get a list of repositories for a given GitHub user."""
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repositories: {response.status_code}")
        return []

def get_readme_url(repo_name, username, token=None):
    """Get the URL of the README file for a given repository."""
    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}/readme"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("download_url")
    else:
        print(f"Failed to fetch README for {repo_name}: {response.status_code}")
        return None

def scrape_readme(readme_url):
    """Scrape the content of the README file."""
    response = requests.get(readme_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch README content: {response.status_code}")
        return None