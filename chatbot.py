import random
import re
from knowledge import KNOWLEDGE_BASE, SYNONYMS, TRIAGE_RULES, MOOD_RESPONSES
from utils import clean_and_tokenize, parse_math_expression, log_conversation, log_error

class SmartMindEngine:
    def __init__(self, memory_module):
        self.memory = memory_module
        self.context = "GENERAL"  # Active Context state

    def match_synonyms(self, tokens):
        """Maps varying input synonyms back to base standardized intent keywords."""
        for i, token in enumerate(tokens):
            for standard_intent, syn_list in SYNONYMS.items():
                if token in syn_list:
                    tokens[i] = standard_intent
        return tokens

    def process_input(self, raw_input):
        """Main NLP structural pipeline with complete error catching and telemetry tracking."""
        try:
            self.memory.profile["stats"]["interactions"] += 1
            
            # 1. Clean input text
            tokens = clean_and_tokenize(raw_input)
            if not tokens:
                return "Input field empty. Communication interface requires character bytes.", "0%", "N/A"
            
            # 2. Run synonym expansion mapping
            tokens = self.match_synonyms(tokens)
            
            # 3. Intercept Master Exit commands
            if "bye" in tokens:
                return random.choice(KNOWLEDGE_BASE["general"]["bye"]), "100%", "Session Control"

            # 4. Math Calculator Processing Check
            math_result = parse_math_expression(raw_input)
            if math_result:
                return math_result, "99%", "Math Core Engine"

            # 5. Emergency Priority Triaging
            for token in tokens:
                if token in TRIAGE_RULES:
                    severity, guidance = TRIAGE_RULES[token]
                    if severity in ["HIGH", "CRITICAL"]:
                        self.memory.profile["stats"]["emergencies"] += 1
                    return f"⚠️ [MEDICAL TRIAGE - SEVERITY: {severity}]: {guidance}", "98%", "Emergency Override"

            # 6. Mood / Sentiment Detection Engine
            for token in tokens:
                if token in MOOD_RESPONSES:
                    return f"💬 [Sentiment Detected]: {MOOD_RESPONSES[token]}", "92%", "Mood Handler"
            
            # 7. Context Switching Logic Matrix
            if "medical" in tokens or "health" in tokens:
                self.context = "HEALTH"
                return "🔄 Context routed: Health Subsystem initialized. Describe your symptoms.", "100%", "Context Switch"
            if "reset" in tokens or "general" in tokens:
                self.context = "GENERAL"
                return "🔄 Context routed: Master General matrix restored.", "100%", "Context Switch"

            # 8. User Profile Memory Ingestion & Recall Check
            memory_store_alert = self.memory.extract_and_store(tokens, raw_input)
            if memory_store_alert:
                return memory_store_alert, "95%", "Memory Matrix"
                
            mem_recall = self.memory.query_memory(tokens)
            if mem_recall:
                return mem_recall, "98%", "Memory Recall Core"
            
            # 9. Intent Domain Lookups
            current_domain = self.context.lower()
            if current_domain in KNOWLEDGE_BASE:
                for token in tokens:
                    if token in KNOWLEDGE_BASE[current_domain]:
                        return random.choice(KNOWLEDGE_BASE[current_domain][token]), "90%", f"Domain: {self.context}"

            # 10. Global Sweep Cross-Domain Fallback Lookup
            for domain in KNOWLEDGE_BASE:
                for token in tokens:
                    if token in KNOWLEDGE_BASE[domain]:
                        return random.choice(KNOWLEDGE_BASE[domain][token]), "80%", f"Cross-Domain ({domain.upper()})"

            return "Input matched vector endpoints but fell below confidence thresholds. Please rephrase.", "0%", "Fallback Routine"

        except Exception as e:
            log_error(f"Execution fault in process_input: {str(e)}")
            return "An internal system fault occurred. Issue logged to error_log.txt.", "0%", "Error Exception"