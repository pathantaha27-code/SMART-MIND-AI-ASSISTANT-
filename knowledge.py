import random

# 1. SYNONYMS VECTOR MATCHING
SYNONYMS = {
    "hello": ["hello", "hi", "hey", "greetings", "morning", "evening", "heyoo"],
    "bye": ["bye", "goodbye", "exit", "terminate", "quit", "leave"],
    "help": ["help", "info", "commands", "guide", "menu"],
    "medical": ["medical", "health", "sick", "pain", "doctor", "symptom"],
    "reset": ["reset", "clear", "general", "normal"]
}

# 2. EXTENDED DOMAIN KNOWLEDGE BASE
KNOWLEDGE_BASE = {
    "general": {
        "hello": [
            "Greetings! I am SmartMind AI, configured to assist Taha Touqir Pathan. How can I help you today?", 
            "Hello! All systems and memory units are operational. What would you like to know?", 
            "Hi there! Ready to run queries or assist with tasks."
        ],
        "help": ["I can handle medical triaging, calculate math, share tech insights, give quotes, or recall Taha's profile and background!"],
        "joke": [
            "Why do programmers wear glasses? Because they can't C#!", 
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
        ],
        "weather": ["Atmospheric telemetry suggests optimal indoor coding conditions!", "Clear conditions forecasted inside the console terminal."],
        "bye": ["Terminating active session safely. Goodbye!", "System entering low-power state. Standby!"]
    },
    "technology": {
        "python": ["Python is an interpreted, high-level language celebrated for clean syntax and powerful automation capabilities."],
        "cpp": ["C++ is a high-performance compiled language known for object-oriented structure and memory management control."],
        "web": ["Front-end web development uses HTML for structure, CSS for styling, and JavaScript for dynamic interactivity."],
        "vscode": ["Visual Studio Code is a powerful lightweight code editor packed with debugging tools and extensions."]
    },
    "sports": {
        "cricket": ["Cricket is a strategic team sport relying on batting precision, bowling tactics, and quick fielding dynamics."],
        "volleyball": ["Volleyball requires high vertical jumps, rapid team communication, sets, spikes, and clean defense."],
        "gym": ["Consistent gym workouts build physical strength, endurance, and mental clarity for long coding sessions!"]
    },
    "motivation": {
        "quote": [
            "The best way to predict the future is to invent it.", 
            "Failure is simply an opportunity to begin again more intelligently.", 
            "Code is like humor. When you have to explain it, it's bad!"
        ]
    }
}

# 3. MEDICAL SEVERITY TRIAGE MATRIX
TRIAGE_RULES = {
    "headache": ("LOW", "Drink water, rest, and minimize screen illumination parameters."),
    "fever": ("MEDIUM", "Monitor body temperature stability, get plenty of rest, and hydrate regularly."),
    "chestpain": ("CRITICAL", "EMERGENCY: Seek immediate medical attention or contact local emergency services instantly!"),
    "bleeding": ("CRITICAL", "EMERGENCY: Apply localized pressure immediately and seek urgent trauma care.")
}

# 4. SENTIMENT RESPONSE DICTIONARY
MOOD_RESPONSES = {
    "happy": "Fantastic! Keeping a positive mindset keeps your focus optimized.",
    "sad": "I am sorry to hear that. Take a break or let's run some calculations and jokes to pass the time.",
    "angry": "Take a deep breath. Let's step back and solve whatever issue is causing strain systematically."
}