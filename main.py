import time
import sys

# --- AVINASH KUMAR'S FINAL DATA (CORRECTED) ---
MY_DATA = {
    "name": "Avinash Kumar",
    "role": "Full Stack / Python Developer",
    "skills": ["Python", "System Design", "App Architecture", "Problem Solving", "Robotics Concepts"],
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
    "contact": "Phone: 8709825303\nEmail: ak6402744@gmail.com",
    "resume_link": "https://drive.google.com/file/d/your-cv-link" 
}

# --- ANIMATION FUNCTIONS ---
def typing_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03) 
    print()

def loading_animation():
    print("\nINITIALIZING AVINASH'S DATABASE...")
    animation = ["[■□□□□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + animation[i] + " CONNECTING...")
        sys.stdout.flush()
    print("\nACCESS GRANTED.\n")

# --- MAIN SYSTEM ---
def start_terminal():
    loading_animation()
    print("========================================")
    typing_print(f"> IDENTITY: {MY_DATA['name']}")
    typing_print(f"> ROLE: {MY_DATA['role']}")
    print("========================================\n")

    # 1. Ask Recruiter Name
    typing_print("> AI: Hello! Before we start, may I know your name?")
    recruiter_name = input("ENTER YOUR NAME: ").strip()
    if recruiter_name == "": recruiter_name = "Recruiter"

    print(f"\n> AI: Welcome, {recruiter_name}. Accessing Avinash's profile...")
    typing_print("> COMMANDS: 'education', 'skills', 'projects', 'contact', 'exit'")
    print("-" * 40)

    while True:
        try:
            user_input = input(f"{recruiter_name}@CMD $> ").lower().strip()
        except EOFError:
            break

        if user_input == "exit":
            typing_print(f"\n> AI: Goodbye {recruiter_name}. Logging off...")
            break
        
        elif user_input == "":
            continue

        print("PROCESSING...")
        time.sleep(0.4) 

        # --- LOGIC ---
        if "hello" in user_input or "hi" in user_input:
            typing_print(f"> AI: Hello {recruiter_name}! Ask me about 'education' or 'projects'.")
        
        elif "education" in user_input or "study" in user_input or "degree" in user_input:
            typing_print(f"> AI: Fetching Academic Records for {MY_DATA['name']}...")
            time.sleep(0.5)
            for edu in MY_DATA['education']:
                print(f"  * {edu}")
                time.sleep(0.2)
        
        elif "skill" in user_input:
            typing_print(f"> AI: Key Technical Skills:")
            typing_print(f"> {', '.join(MY_DATA['skills'])}")
            
        elif "project" in user_input:
            typing_print("> AI: Loading Project Portfolio...")
            for proj in MY_DATA['projects']:
                time.sleep(0.2)
                print(f"  - {proj}")

        elif "contact" in user_input or "hire" in user_input:
            typing_print(f"> AI: Contact Details:")
            print(f"{MY_DATA['contact']}")
            
        else:
            typing_print(f"> AI: Invalid Command. Try typing 'education' or 'contact'.")
        
        print("-" * 40)

if __name__ == "__main__":
    start_terminal()
