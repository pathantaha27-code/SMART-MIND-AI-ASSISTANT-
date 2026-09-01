import time
from memory import SmartMemory
from chatbot import SmartMindEngine

def print_loading_bar():
    """Renders high-grade enterprise software loading modules onto console layout."""
    print("\nInitializing SmartMind Core Components...")
    modules = ["Memory Registry", "NLP Engine Router", "Structural Matrices"]
    for module in modules:
        print(f"Loading {module:20} [", end="")
        for _ in range(12):
            print("█", end="")
            time.sleep(0.03)
        print("] 100% ✓")
    time.sleep(0.2)

def display_welcome_banner():
    """Displays the master structural system boot layout profile."""
    print("\n" + "="*45)
    print("         SMARTMIND AI ASSISTANT CORE         ")
    print("="*45)
    print(" Version : 2.0.0 Base Architecture")
    print(" System Status: Core Operational")
    print("-" * 45)
    print(" Active Commands: general | medical | reset | bye")
    print(" Memory Triggers: My favorite sport is X")
    print("                  What is my favorite sport?")
    print("-" * 45)

def run_chat_loop(engine, memory):
    """Main execution loop for user interactions."""
    username = input("\nSystem prompt: Declare username to open socket.\nUser: ").strip()
    if username:
        memory.profile["user_name"] = username
        
    print(f"\nAssistant: Socket secure. Welcome back, {memory.profile['user_name']}.\n")
    
    while True:
        raw_input = input(f"{memory.profile['user_name']}: ")
        if not raw_input.strip():
            continue
            
        response, confidence, intent_class = engine.process_input(raw_input)
        
        # Meta telemetry logging
        print(f"Telemetry -> Match: {intent_class:18} | Conf: {confidence}")
        print(f"Assistant: {response}\n")
        
        if "Terminating active session" in response or response in ["Terminating active session safely. Goodbye!", "System entering low-power state. Standby!"]:
            break

def main_menu():
    """Master UI interface selecting project runtime vectors."""
    memory = SmartMemory()
    engine = SmartMindEngine(memory)
    
    print_loading_bar()
    
    while True:
        display_welcome_banner()
        print(" [1] Launch SmartMind Engine Chat Terminal")
        print(" [2] View System Specifications Architecture")
        print(" [3] Exit Framework Application")
        print("-" * 45)
        
        choice = input("Select System Operations Vector (1-3): ").strip()
        
        if choice == "1":
            run_chat_loop(engine, memory)
        elif choice == "2":
            print("\n" + "-"*40)
            print("         SYSTEM CONFIGURATION SCHEMATICS       ")
            print("-"*40)
            print(" NLP Parsing Engine : Token-level Regex Array Router")
            print(" Memory Sub-allocator: Persistent Dynamic Object Class")
            print(" Context Execution  : State-Aware Conditional Tracking")
            print("-"*40 + "\n")
            input("Press Enter to return to Master Control Menu...")
        elif choice == "3":
            print("\nExiting Framework Runtime Interface. System Off.")
            break
        else:
            print("\nInvalid operation matrix coordinate selected. Please try again.")

if __name__ == "__main__":
    main_menu()