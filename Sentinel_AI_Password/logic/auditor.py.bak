from zxcvbn import zxcvbn
from logic.model_ladder import ModelLadder

class PasswordAuditor:
    def __init__(self, llm: ModelLadder):
        self.llm = llm

    def check_math(self, password: str) -> dict:
        """
        Analyzes a password using zxcvbn.
        
        Args:
            password: The password to analyze.
            
        Returns:
            A dictionary containing zxcvbn results (score, crack_times, feedback).
        """
        if not password:
            return {}
        
        results = zxcvbn(password)
        return results

    def roast_password(self, password: str) -> str:
        """
        Roasts the password using a 'Red Team Hacker' persona.
        
        Args:
            password: The password to roast.
            
        Returns:
            A string containing the critique.
        """
        if not password:
            return "Give me a password to crack, rookie."

        # System prompt for the persona
        system_prompt = (
            "You are a cynical, elite Red Team Hacker. "
            "Your job is to roast the user's password security. "
            "Explain exactly how it would be cracked (e.g., dictionary attack, brute force, social engineering). "
            "Be cruel but educational. "
            "If the password is actually good, begrudgingly admit it but warn them to stay vigilant. "
            "Keep it short and punchy (max 3 sentences)."
        )
        
        query = f"{system_prompt}\n\nPassword: {password}"
        
        response = self.llm.invoke(query)
        return response.content.strip()
