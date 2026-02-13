import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

import logging

# Configure logging
logging.basicConfig(filename='sentinelxc.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ModelLadder:
    def __init__(self):
        self.models = []
        
        # Helper to get key from secrets or env
        def get_key(name):
            # Check Streamlit secrets first
            try:
                if hasattr(st, "secrets") and name in st.secrets:
                    return st.secrets[name]
            except FileNotFoundError:
                # Secrets file doesn't exist locally, which is fine
                pass
            except Exception as e:
                logging.warning(f"Error accessing st.secrets: {e}")
            
            # Fallback to os.getenv
            return os.getenv(name)
        
        # 1. Primary: Gemini
        google_key = get_key("GOOGLE_API_KEY")
        if google_key:
            try:
                self.models.append({
                    "name": "Gemini 2.0 Flash",
                    "llm": ChatGoogleGenerativeAI(
                        model="gemini-2.0-flash",
                        google_api_key=google_key,
                        temperature=0.1
                    )
                })
            except Exception as e:
                 logging.error(f"Failed to load Gemini: {e}")

        # 2. Secondary: Groq (Llama 3)
        groq_key = get_key("GROQ_API_KEY")
        if groq_key:
            try:
                self.models.append({
                    "name": "Llama 3.3 (Groq)",
                    "llm": ChatGroq(
                        model_name="llama-3.3-70b-versatile",
                        groq_api_key=groq_key,
                        temperature=0.9
                    )
                })
            except Exception as e:
                logging.error(f"Failed to load Groq: {e}")
            
        # 3. Tertiary: Mistral
        mistral_key = get_key("MISTRAL_API_KEY")
        if mistral_key:
            try:
                self.models.append({
                    "name": "Mistral Tiny",
                    "llm": ChatMistralAI(
                        model="mistral-tiny",
                        mistral_api_key=mistral_key,
                        temperature=0.7
                    )
                })
            except Exception as e:
                logging.error(f"Failed to load Mistral: {e}")
            
        if not self.models:
            logging.error("No models loaded. Please checks your .env file or Streamlit Secrets for API keys.")
            raise ValueError("No AI models available. Please check environment configuration.")

    def invoke(self, prompt: str):
        """
        Iterates through the model ladder until one succeeds.
        """
        errors = []
        for model_entry in self.models:
            name = model_entry["name"]
            llm = model_entry["llm"]
            
            try:
                logging.info(f"Attempting invoke with {name}")
                response = llm.invoke(prompt)
                return response
            except Exception as e:
                error_msg = f"{name} failed: {str(e)}"
                logging.warning(error_msg)
                errors.append(error_msg)
                # Continue to next model
                
        # If we reach here, all models failed
        logging.critical("All models in the ladder failed.")
        raise Exception(f"All models failed. Errors: {'; '.join(errors)}")
