# Github-Project-Summarizer

A Streamlit application that automatically summarizes GitHub repositories using LLMs. This tool helps developers create concise project summaries suitable for CVs and portfolios.

## Features

- Fetches repositories from a given GitHub username
- Extracts and processes README files
- Generates concise summaries using LLMs to put in your CV
- Exports summaries in LaTeX in a txt file

## Requirements

- Python 3.x
- OpenAI API key
- GitHub token (optional)

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_key_here
```

## Usage

1. Run the application with the following command:

```bash
 `streamlit run app.py`
```

2. Enter a GitHub username
3. Wait for the processing to complete
4. Download the generated summaries