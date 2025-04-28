import re
 from typing import Tuple
 
 def validate_password(password: str) -> Tuple[bool, str]:
     """
     Validates a password against security requirements.
     
     Requirements:
     - Minimum 8 characters
     - Maximum 24 characters
     - At least one uppercase letter
     - At least one lowercase letter
     - At least one number
     - At least one special character
     
     Returns:
         Tuple[bool, str]: (is_valid, error_message)
     """
     if len(password) < 8:
         return False, "Password must be at least 8 characters long"
     
     if len(password) > 24:
         return False, "Password must not exceed 24 characters"
     
     if not re.search(r'[A-Z]', password):
         return False, "Password must contain at least one uppercase letter"
     
     if not re.search(r'[a-z]', password):
         return False, "Password must contain at least one lowercase letter"
     
     if not re.search(r'[0-9]', password):
         return False, "Password must contain at least one number"
     
     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
         return False, "Password must contain at least one special character"
     
     return True, "Password is valid"