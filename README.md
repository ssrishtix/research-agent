# Research-Agent

A tool that gathers, analyzes, and summarizes information about companies and roles using AI APIs.

---

## Features

- Aggregate data about companies and job roles
- Summarize key information for quick insights
- Easily configurable API access via environment variables

---

## Requirements

- Python 3.8+
- API key for the AI service (e.g., OpenAI API key)
- Required Python packages (see below)

---

## Installation

1. Clone this repository:

   \```bash
   git clone https://github.com/yourusername/research-agent.git
   cd research-agent
   \```

2. Create and activate a virtual environment:

   \```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \```

3. Install dependencies:

   \```bash
   pip install -r requirements.txt
   \```

---

## Setup API Key

You must have an API key from the AI provider you use (e.g., [OpenAI](https://platform.openai.com/account/api-keys)).

Set your API key as an environment variable:

- On macOS/Linux (bash/zsh):

  \```bash
  export OPENAI_API_KEY="your_api_key_here"
  \```

- On Windows (PowerShell):

  \```powershell
  setx OPENAI_API_KEY "your_api_key_here"
  \```

The project reads this environment variable at runtime.

---

## Usage

Run the main script with the required arguments:

\```bash
python run_agent.py --company "CompanyName" --role "RoleName"
\```

Additional options:

- \`--limit\` : Number of data sources to aggregate (default: 3)
- \`--outpath\` : Path to save the output JSON summary

Example:

\```bash
python run_agent.py --company "Google" --role "Software Engineer" --limit 5 --outpath output/google_se.json
\```

---

## Notes

- **Do not** hardcode or commit your API key to GitHub.
- Keep your \`.env\` or any config files containing secrets in \`.gitignore\`.
- Always protect your API keys and rotate them if you suspect leakage.

---

## Contributing

Feel free to open issues or pull requests to improve the project.
