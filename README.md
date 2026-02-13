# Sentinel - The AI Password Architect & Auditor 🛡️

Sentinel is a Streamlit-based web application that leverages Google's Gemini Pro model to generate high-entropy, memorable passwords and audit existing passwords with a "Red Team Hacker" persona.

## features

- **Password Architect**: Generates memorable XKCD-style passwords based on a user-provided theme (e.g., "Cyberpunk City").
- **Red Team Audit**: Analyzes password strength using `zxcvbn` (mathematical estimation of entropy) and provides a unique "roast" from an AI hacker persona explaining *how* it would be cracked.

## prerequisites

- Python 3.10+
- A Google Cloud API Key with access to Gemini API.

## setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Sentinel_AI_Password
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv environ
    source environ/bin/activate  # On Windows: environ\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    - Rename `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
    - Open `.env` and add your Google API Key:
        ```
        GOOGLE_API_KEY=your_api_key_here
        ```

## usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Opens in your browser at `http://localhost:8501`.

## project structure

```
Sentinel_AI_Password/
├── app.py                 # Main UI entry point
├── .env                   # Local secrets (ignored by git)
├── logic/
│   ├── generator.py       # Theme-to-Password Logic
│   └── auditor.py         # zxcvbn + Hacker Persona Logic
└── ui/
    └── styles.py          # Custom CSS/Styling
```
