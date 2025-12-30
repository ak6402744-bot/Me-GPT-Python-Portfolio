import time
import sys

# --- AVINASH KUMAR'S ULTIMATE DATABASE ---
MY_DATA = {
    "name": "Avinash Kumar",
    "role": "Full Stack / Python Developer",
    "skills": ["Python", "System Design", "Logic Building", "Problem Solving", "Robotics Concepts"],
    "projects": [
        "1. Kabad-to-Bot (AI-based E-waste Recycling System)",
        "2. Gali-Connect (Hyper-local Vendor Tracking App)",
        "3. Me-GPT (Interactive AI Portfolio - Self Built)"
    ],
    "education": [
        "MCA (Master of Computer Applications)\n    Ranchi University | Passing Year: 2021 | Score: 75.00%",
        "BCA (Bachelor of Computer Applications)\n    Punjab Technical University | Passing Year: 2014 | Score: 70.00%",
        "12th Intermediate\n    Bokaro Ispat Sr. Sec. School | Passing Year: 2012 | Score: 59%",
        "10th Board\n    GGPS School | Passing Year: 2008 | Score: 65%"
    ],
    "contact": "Phone: 8709825303\nEmail: ak6402744@gmail.com"
}

# --- ANIMATION EFFECT ---
def typing_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03) 
    print()

# --- NEW FEATURE: MATH EXPERT MODE ---
def math_expert():
    typing_print("\n[MATH MODE ACTIVATED] 🧮")
    typing_print("> AI: I can solve math for you now! (Type 'back' to return to menu)")
    while True:
        exp = input("MATH@AI $> ").strip().lower()
        if exp == 'back': 
            typing_print("> AI: Exiting Math Mode...")
            break
        try:
            # Using eval to process mathematical string
            result = eval(exp)
            print(f"RESULT: {result}")
        except Exception:
            print("Error: Invalid calculation. Example: (50 * 2) + 10")

# --- MAIN SYSTEM ---
def start_terminal():
    print("\n" + "="*40)
    print("INITIALIZING AVINASH'S ADVANCED AI CLONE...")
    print("="*40)
    time.sleep(1)
    
    typing_print(f"> IDENTITY: {MY_DATA['name']}")
    typing_print(f"> ROLE: {MY_DATA['role']}")
    print("-" * 40)

    # Ask for Recruiter's Name
    typing_print("> AI: Hello! I am Avinash's AI clone. What is your name?")
    recruiter_name = input("ENTER YOUR NAME: ").strip()
    if not recruiter_name: recruiter_name = "Recruiter"

    print(f"\n> AI: Welcome, {recruiter_name}. Accessing my neural records...")
    typing_print("> COMMANDS: 'education', 'skills', 'projects', 'calc', 'contact', 'exit'")
    print("-" * 40)

    while True:
        try:
            user_input = input(f"{recruiter_name}@CMD $> ").lower().strip()
        except EOFError: break

        if user_input == "exit":
            typing_print(f"\n> AI: Logging off. Goodbye {recruiter_name}!")
            break
        elif user_input == "": continue

        # --- LOGIC HANDLING ---
        print("PROCESSING...")
        time.sleep(0.3)

        if user_input == "calc":
            math_expert()
        elif "education" in user_input or "study" in user_input:
            typing_print("> AI: Academic History Loaded:")
            for edu in MY_DATA['education']:
                print(f"  * {edu}")
                time.sleep(0.1)
        elif "skill" in user_input:
            typing_print(f"> AI: Technical Skills: {', '.join(MY_DATA['skills'])}")
        elif "project" in user_input:
            typing_print("> AI: Project Portfolio:")
            for proj in MY_DATA['projects']:
                print(f"  - {proj}")
                time.sleep(0.1)
        elif "contact" in user_input:
            typing_print(f"> AI: Reach me at:\n{MY_DATA['contact']}")
        else:
            typing_print(f"> AI: Sorry {recruiter_name}, I don't recognize that command. Try 'calc' or 'education'.")
        
        print("-" * 40)

if __name__ == "__main__":
    start_terminal()
