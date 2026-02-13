import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from logic import generator, auditor
from ui import styles

# Load env variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Sentinel - Password Architect & Auditor",
    page_icon="🛡️",
    layout="centered"
)

# Apply Styles
styles.apply_custom_styles()

from logic.model_ladder import ModelLadder

# ...

@st.cache_resource
def get_llm():
    """
    Initializes the Model Ladder (Gemini -> Groq -> Mistral).
    """
    return ModelLadder()

st.title("🛡️ Sentinel AI")
st.subheader("The AI Password Architect & Auditor")

# Initialize LLM
try:
    llm = get_llm()
except Exception as e:
    st.error(f"Failed to initialize LLM: {str(e)}")
    st.stop()

# Tabs
tab1, tab2 = st.tabs(["🛡️ Architect", "💀 Red Team Audit"])

# --- GENERAOR TAB ---
with tab1:
    st.header("Password Generator")
    st.markdown("Create a high-entropy, memorable password based on a vibe.")
    
    theme = st.text_input("Enter a Theme (e.g., 'Cyberpunk City', 'Tropical Beach')", value="Space Exploration", max_chars=64)
    
    if st.button("Generate Password", type="primary"):
        with st.spinner("Consulting the architect..."):
            try:
                password = generator.generate_memorable_password(theme, llm)
                st.success("Generated Password:")
                st.code(password, language=None)
                st.info("Copy this password and store it safely.")
            except Exception as e:
                st.error(f"Error generating password: {str(e)}")

# --- AUDIT TAB ---
with tab2:
    st.header("Red Team Audit")
    st.markdown("Analyze your password's strength and get roasted by an AI hacker.")
    
    password_input = st.text_input("Enter Password to Audit", type="password", max_chars=128)
    
    if st.button("Audit Password", type="primary"):
        if not password_input:
            st.warning("Please enter a password.")
        else:
            with st.spinner("Analyzing with zxcvbn and Red Team Persona..."):
                try:
                    # Initialize Auditor
                    audit_tool = auditor.PasswordAuditor(llm)
                    
                    # 1. zxcvbn check
                    stats = audit_tool.check_math(password_input)
                    score = stats['score']  # 0 to 4
                    crack_time = stats['crack_times_display']['offline_slow_hashing_1e4_per_second']
                    feedback = stats['feedback'].get('warning')
                    suggestions = stats['feedback'].get('suggestions')
                    
                    # 2. LLM Roast
                    roast = audit_tool.roast_password(password_input)
                    
                    # --- DASHBOARD ---
                    st.markdown("### 📊 Security Analysis Dashboard")
                    
                    # Score Progress Bar
                    st.write(" **Security Score**")
                    score_labels = ["💀 Critical", "⚠️ Weak", "🤔 Moderate", "🛡️ Strong", "🔥 Unbreakable"]
                    st.progress(score / 4, text=f"{score}/4 - {score_labels[score]}")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric(label="Estimated Crack Time", value=crack_time)
                    
                    with col2:
                        if score < 3:
                            st.error("Verdict: VULNERABLE")
                        else:
                            st.success("Verdict: SECURE")

                    if feedback:
                        st.warning(f"**Warning:** {feedback}")
                    
                    if suggestions:
                        st.info(f"**Tip:** {suggestions[0]}")
                    
                    # Composition Chart
                    st.write("### 🧬 Password Composition")
                    composition = {
                        "Lowercase": sum(1 for c in password_input if c.islower()),
                        "Uppercase": sum(1 for c in password_input if c.isupper()),
                        "Numbers": sum(1 for c in password_input if c.isdigit()),
                        "Symbols": sum(1 for c in password_input if not c.isalnum())
                    }
                    st.bar_chart(composition)

                    st.markdown("---")
                    st.markdown("### 👺 Red Team Roast")
                    st.caption("AI Hacker Persona")
                    st.markdown(f"> *{roast}*")
                    
                except Exception as e:
                    st.error(f"Error during audit: {str(e)}")
