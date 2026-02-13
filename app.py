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
    
    theme = st.text_input("Enter a Theme (e.g., 'Cyberpunk City', 'Tropical Beach')", value="Space Exploration")
    
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
    
    password_input = st.text_input("Enter Password to Audit", type="password")
    
    if st.button("Audit Password", type="primary"):
        if not password_input:
            st.warning("Please enter a password.")
        else:
            with st.spinner("Analyzing with zxcvbn and Red Team Persona..."):
                try:
                    # Initialize Auditor
                    audit_tool = auditor.PasswordAuditor(llm)
                    
                    # Math Check
                    math_result = audit_tool.check_math(password_input)
                    score = math_result.get('score', 0)
                    crack_times = math_result.get('crack_times_display', {})
                    feedback = math_result.get('feedback', {})

                    # Roast
                    roast = audit_tool.roast_password(password_input)
                    
                    # Display Results
                    st.markdown("### 📊 Security Score")
                    
                    # Progress bar
                    progress_val = score / 4.0
                    st.progress(progress_val)
                    st.write(f"**Score: {score}/4**")
                    
                    st.write(f"**Time to Crack (Offline Fast Hashing):** {crack_times.get('offline_fast_hashing_1e10_per_second', 'N/A')}")
                    
                    if feedback.get('warning'):
                        st.warning(f"⚠️ {feedback['warning']}")
                    if feedback.get('suggestions'):
                        for suggestion in feedback['suggestions']:
                            st.info(f"💡 {suggestion}")

                    st.markdown("---")
                    st.markdown("### 😈 Red Team Roast")
                    st.write(roast)
                    
                except Exception as e:
                    st.error(f"Error during audit: {str(e)}")
