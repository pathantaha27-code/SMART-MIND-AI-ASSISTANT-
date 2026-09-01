import re

class SmartMemory:
    def __init__(self):
        # Pre-loaded Profile for Taha Touqir Pathan
        self.profile = {
            "user_name": "Taha Touqir Pathan",
            "age": 18,
            "education": "Grade 11 Computer Science & Data Entry Student (NIOS Class 10 Graduate)",
            "origin": "Junagadh, Gujarat, India",
            "current_location": "Mansa, Luapula Province, Zambia",
            "favorite_sports": ["Cricket", "Volleyball"],
            "technical_skills": ["Python", "C++", "HTML", "CSS", "JavaScript", "VS Code"],
            "fitness": "Gym Workouts",
            "favorite_editor": "VS Code",
            "stats": {
                "interactions": 0,
                "questions": 0,
                "emergencies": 0
            }
        }
    
    def extract_and_store(self, tokens, raw_text):
        """Rule-based text analysis to intercept and extract personal attributes dynamically."""
        raw_text_lower = raw_text.lower()
        
        if "sport" in tokens and "is" in tokens:
            match = re.search(r"sport is\s+([a-zA-Z]+)", raw_text_lower)
            if match:
                sport = match.group(1).capitalize()
                self.profile["favorite_sports"].append(sport)
                return f"Memory updated: New sport logged as [{sport}]."
            
        if "language" in tokens and "is" in tokens:
            match = re.search(r"language is\s+([a-zA-Z\+\#]+)", raw_text_lower)
            if match:
                lang = match.group(1).capitalize()
                self.profile["technical_skills"].append(lang)
                return f"Memory updated: Technical skill logged as [{lang}]."
            
        return None

    def query_memory(self, tokens):
        """Retrieves stored background and profile attributes instantly."""
        # Convert tokens list to a single lowercase string for easy keyword checking
        input_str = " ".join(tokens).lower()
        
        # 1. Location & Origins
        if any(word in tokens for word in ["from", "origin", "born", "live", "reside", "location"]):
            return f"Taha was born in {self.profile['origin']} and is currently living in {self.profile['current_location']}!"

        # 2. Education & Studies
        if any(word in tokens for word in ["study", "studying", "education", "grade", "class", "school"]):
            return f"Taha is an 18-year-old {self.profile['education']}!"

        # 3. Hobbies & Sports
        if any(word in tokens for word in ["hobby", "hobbies", "sport", "sports", "game", "games"]):
            sports_str = ", ".join(self.profile["favorite_sports"])
            return f"Taha's primary hobbies include playing {sports_str}, gym workouts, and coding web applications!"

        # 4. Tech Stack & Skills
        if any(word in tokens for word in ["skill", "skills", "code", "coding", "tech", "programming", "languages"]):
            skills_str = ", ".join(self.profile["technical_skills"])
            return f"Taha's technical stack includes: {skills_str}!"

        # 5. Fun Specific Queries
        if any(word in tokens for word in ["editor", "ide", "environment", "vscode"]):
            return f"Taha's favorite coding environment is Visual Studio Code ({self.profile['favorite_editor']})!"
        if "frontend" in input_str or "backend" in input_str:
            return "Taha enjoys crafting clean front-end web interfaces using HTML, CSS, and JS, while building solid back-end logic in Python and C++!"

        return None