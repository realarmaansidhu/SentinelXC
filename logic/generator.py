import random
import string
import re
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
        "Return ONLY a space-separated list of the 4 words (e.g., 'Hammer Anvil Spark Fire'). "
        "Do NOT include numbers, bullet points, or introductory text."
    )
    
    response = llm.invoke(query)
    content = response.content.strip()
    
    # Robust extraction using Regex
    # Find all words that are at least 3 characters long to avoid 'a', 'the', etc.
    found_words = re.findall(r'\b[a-zA-Z]{3,}\b', content)
    
    # Deduplicate while preserving order
    seen = set()
    words = [x for x in found_words if not (x.lower() in seen or seen.add(x.lower()))]
    
    # Ensure we have at least 4 words
    if len(words) < 4:
        # Fallback list tailored to the theme concept if possible, or generic
        words = ["Cyber", "Neon", "Future", "System"] 
    
    words = words[:4] # Take first 4
    
    # Capitalize
    words = [w.capitalize() for w in words]
    
    # Separators
    special_chars = "#-!@$%^&*"
    separator = random.choice(special_chars)
    
    # Add a number
    number = str(random.randint(0, 99))
    
    password = separator.join(words) + str(number)
    
    return password
