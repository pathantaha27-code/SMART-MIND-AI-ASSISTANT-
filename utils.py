import re
import time
import sys
from datetime import datetime

def clean_and_tokenize(text):
    """Uses advanced regular expressions to accurately isolate clean text tokens."""
    return re.findall(r"\b\w+\b", text.lower())

def get_timestamp():
    """Returns standard clock telemetry format string."""
    return datetime.now().strftime("%I:%M:%S %p")

def log_conversation(user, message, assistant_response):
    """Appends active conversation arrays to disk logs for history inspection."""
    timestamp = get_timestamp()
    try:
        with open("conversation_history.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] User ({user}): {message}\n")
            file.write(f"[{timestamp}] Assistant: {assistant_response}\n\n")
    except Exception as e:
        log_error(f"IO Write Failure: {str(e)}")

def log_error(error_message):
    """Records exceptions securely inside an internal error management file."""
    timestamp = get_timestamp()
    try:
        with open("error_log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] EXCEPTION ENCOUNTERED: {error_message}\n")
    except:
        pass

def parse_math_expression(text):
    """Safely extracts and evaluates mathematical calculations."""
    cleaned = re.sub(r"[^\d\+\-\*\/\.\(\)]", "", text)
    if not cleaned or not any(char in text for char in ["+", "-", "*", "/"]):
        return None
    try:
        # Safely evaluate numeric expression matrix
        result = eval(cleaned, {"__builtins__": None}, {})
        return f"Calculated Result: {cleaned} = {result}"
    except:
        return None