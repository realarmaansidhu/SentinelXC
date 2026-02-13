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
        
        # 1. Primary: Gemini
        google_key = os.getenv("GOOGLE_API_KEY")
        if google_key:
            self.models.append({
                "name": "Gemini 2.0 Flash",
                "llm": ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash",
                    google_api_key=google_key,
                    temperature=0.1
                )
            })
            
        # 2. Secondary: Groq (Llama 3)
        groq_key = os.getenv("GROQ_API_KEY")
        if groq_key:
            self.models.append({
                "name": "Llama 3.3 (Groq)",
                "llm": ChatGroq(
                    model_name="llama-3.3-70b-versatile",
                    groq_api_key=groq_key,
                    temperature=0.9
                )
            })
            
        # 3. Tertiary: Mistral
        mistral_key = os.getenv("MISTRAL_API_KEY")
        if mistral_key:
            self.models.append({
                "name": "Mistral Tiny",
                "llm": ChatMistralAI(
                    model="mistral-tiny",
                    mistral_api_key=mistral_key,
                    temperature=0.7
                )
            })
            
        if not self.models:
            logging.error("No models loaded. Please checks your .env file for API keys.")
            raise ValueError("No AI models available. Please check your .env file.")

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
