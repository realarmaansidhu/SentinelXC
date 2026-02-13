import streamlit as st

def apply_custom_styles():
    """
    Applies custom CSS to the Streamlit app.
    """
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #00FF94 !important; /* Cyberpunk Green */
            font-family: 'Courier New', Courier, monospace;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #00FF94;
            color: #0E1117;
            border-radius: 5px;
            font-weight: bold;
            border: none;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #00CC76;
            color: #FFFFFF;
            box-shadow: 0 0 10px #00FF94;
        }
        
        /* Input fields */
        .stTextInput>div>div>input {
            background-color: #262730;
            color: #FAFAFA;
            border: 1px solid #4F4F4F;
            border-radius: 5px;
        }

        /* Labels */
        .stTextInput>label, .stSelectbox>label {
            color: #00FF94 !important;
            font-weight: bold;
        }

        /* Markdown Text */
        .stMarkdown p {
            color: #FAFAFA;
        }

        /* Progress bar */
        .stProgress > div > div > div > div {
            background-color: #00FF94;
        }
        
        /* Metric Labels */
        [data-testid="stMetricLabel"] {
            color: #00FF94 !important;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #1F1F1F;
            border-radius: 5px;
            padding: 10px 20px;
            color: #FAFAFA;
        }

        .stTabs [aria-selected="true"] {
            background-color: #00FF94 !important;
            color: #0E1117 !important;
        }

        </style>
        """, unsafe_allow_html=True)
