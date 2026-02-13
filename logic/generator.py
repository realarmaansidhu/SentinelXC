import random
import string
from logic.model_ladder import ModelLadder

def generate_memorable_password(theme: str, llm: ModelLadder) -> str:
    """
    Generates a high-entropy, memorable password based on a theme.
    
    Args:
        theme: The user's chosen theme or vibe.
        llm: An initialized ModelLadder instance.
        
    Returns:
        A generated password string.
    """
    if not theme:
        theme = "random"

    # prompt for 4 distinct concrete objects
    query = (
        f"Generate 4 random, distinct, concrete objects related to '{theme}'. "
        "Return ONLY a space-separated list of the 4 words. "
        "Do not include any other text or numbering."
    )
    
    response = llm.invoke(query)
    content = response.content.strip()
    
    # Split the response into words
    # Handle cases where the model might output newlines or commas
    words = content.replace(",", " ").split()
    
    # Ensure we have at least 4 words, if not, fallback or use what we have
    if len(words) < 4:
        # Fallback if model fails to output 4 words (unlikely with this model but possible)
        words = ["Correct", "Horse", "Battery", "Staple"] 
    
    words = words[:4] # Take first 4
    
    # Clean words (remove punctuation if any slipped in, capitalize)
    words = [w.strip(string.punctuation).capitalize() for w in words]
    
    # Separators
    special_chars = "#-!@$%^&*"
    separator = random.choice(special_chars)
    
    # Add a number
    number = str(random.randint(0, 99))
    
    password = separator.join(words) + str(number)
    
    return password
