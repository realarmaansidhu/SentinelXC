# 🛡️ SentinelXC - Password Architect & Auditor

![SentinelXC Login](https://img.shields.io/badge/Status-Stable-brightgreen) ![Python 3.12](https://img.shields.io/badge/Python-3.12-blue) ![UI-Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

> **"The only secure password is the one you can't remember. But SentinelXC makes it memorable."**

**SentinelXC** is a next-generation cybersecurity tool that combines **generative AI** with traditional security algorithms. It serves two main purposes:
1.  **Architect**: Generating high-entropy, memorable passwords based on user themes (XKCD-style).
2.  **Auditor**: analyzing password strength using mathematical models and an AI "Red Team" persona that roasts your security choices.

---

## 🚀 Features

### 1. 🏗️ The Architect
Forget "Tr0ub4dor&3". Tell Sentinel a theme like *"Cyberpunk City"* or *"Tropical Beach"*, and it will generate a cryptographically strong yet memorable password such as:
> `Neon#Keyboard#Motorcycle#Helmet44`

### 2. 💀 Red Team Audit
We combine **zxcvbn** (Dropbox's entropy estimator) with a **Large Language Model (LLM)** configured as a ruthless brilliant hacker.
- **Quantitative**: Score (0-4), Crack Time, and offline hashing analysis.
- **Qualitative**: A biting, sarcastic roast of your password's weaknesses.

### 3. 🧗 The Model Ladder
**SentinelXC** is built for resilience. It features a fail-safe **Model Ladder** that automatically switches providers if one is rate-limited or down.

```mermaid
graph TD
    A[Request Password/Audit] --> B{Gemini 2.0 Flash}
    B -->|Success| C[Return Result]
    B -->|Fail| D{Llama 3 (Groq)}
    D -->|Success| C
    D -->|Fail| E{Mistral Tiny}
    E -->|Success| C
    E -->|Fail| F[Error Handling]
```

### 4. 🛡️ Enterprise-Grade Security
- **Prompt Injection Defense**: Inputs are sandboxed in triple quotes and truncated to prevent LLM hijacking.
- **DoS Protection**: Strict input length limits prevent context window exhaustion attacks.
- **Fail-Safe Logging**: Comprehensive error tracking for the Model Ladder.

---

## 🔮 Future Roadmap

We are building the ultimate AI Security Suite. Coming soon:

### 📂 Phase 2: Batch Operations
- **Bulk Auditor**: Upload `.csv` or `.txt` files to audit thousands of passwords at once.
- **Factory Mode**: Generate batch passwords (e.g., 500x) for enterprise provisioning.

### 🔌 Phase 3: Integration
- **API Endpoint**: REST API to integrate SentinelXC's logic into your own apps.
- **Browser Extension**: Real-time password strength analysis in your browser.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) with custom CSS for a "Cyber Security" aesthetic.
- **Orchestration**: [LangChain](https://www.langchain.com/).
- **AI Models**:
    - **Primary**: Google Gemini 2.0 Flash (`langchain-google-genai`)
    - **Secondary**: Llama 3 on Groq (`langchain-groq`)
    - **Tertiary**: Mistral AI (`langchain-mistralai`)
- **Security Logic**: `zxcvbn` (Python port).

---

## 📦 Installation

## How to Run
1.  **Clone**: `git clone https://github.com/realarmaansidhu/SentinelAI.git`
2.  **Navigate**: `cd SentinelAI`
3.  **Install**: `pip install -r requirements.txt`
4.  **Run**: `streamlit run app.py`

3.  **Configure Environment**:
    Create a `.env` file (copy from `.env.example`) and add your API keys:
    ```ini
    GOOGLE_API_KEY=your_gemini_key
    GROQ_API_KEY=your_groq_key
    MISTRAL_API_KEY=your_mistral_key
    ```

4.  **Run the App**:
    ```bash
    streamlit run app.py
    ```

---

## 📸 Screenshots

| Architect Mode | Red Team Mode |
|:---:|:---:|
| Generate themed passwords | Get roasted by AI |

---

Made with ❤️ and ☕ by [Armaan Sidhu](https://github.com/realarmaansidhu)
