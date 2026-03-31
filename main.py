import pandas as pd
import numpy as np
import sys
import time
import os
import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# --- ⚙️ Configuration & setup ---
FEATURES = ["study_hours", "sleep_hours", "screen_time", "stress_level", "exercise_hours", "caffeine_cups"]
DATA_FILE = "data.csv"
HISTORY_FILE = "prediction_history.csv"

def get_recommendation(vals):
    """Generates a detailed, emoji-rich solution based on the most critical metric."""
    study, sleep, screen, stress, exercise, caffeine = vals
    
    suggestions = []
    if stress >= 8: 
        suggestions.append("🧘 High Stress: Try the 4-7-8 breathing method or a 5-minute guided meditation.")
    if sleep < 6: 
        suggestions.append("🌙 Sleep Debt: Power down all screens 60 mins before bed to boost melatonin.")
    if exercise < 0.5: 
        suggestions.append("🏃 Inactivity: A quick 15-min walk can increase blood flow to the brain and reset focus.")
    if screen > 5: 
        suggestions.append("👀 Screen Fatigue: Follow the 20-20-20 rule to prevent digital eye strain.")
    if study > 8: 
        suggestions.append("🧠 Brain Fog: Use Pomodoro (50/10) to avoid 'diminishing returns' on your study time.")
    if caffeine > 4: 
        suggestions.append("☕ Caffeine Overload: Switch to herbal tea after 2 PM to protect your deep sleep cycle.")
    
    # Return the top priority or a general positive message
    return suggestions[0] if suggestions else "🌟 Balance: You're doing great! Keep maintaining this sustainable routine."

def clear_history():
    """Interactive history cleanup."""
    if not os.path.exists(HISTORY_FILE):
        print("\n📂 [System] History is already clean!")
        return

    print("\n" + "!"*40)
    confirm = input(" ⚠️  DANGER ZONE: Clear all records? (Type 'yes' to wipe): ").lower()
    if confirm == 'yes':
        os.remove(HISTORY_FILE)
        print(" ✨ [System] History has been vaporized!")
    else:
        print(" 💨 [System] Cleanup cancelled.")
    time.sleep(1.2)

def save_to_history(name, age, inputs, probability, result, solution):
    file_exists = os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Name", "Age"] + FEATURES + ["Prob", "Status", "Recommendation"])
        timestamp = time.strftime("%Y-%m-%d %H:%M")
        status = "🔥 High Risk" if result == 1 else "🌿 Low Risk"
        writer.writerow([timestamp, name, age] + inputs + [f"{probability:.2%}", status, solution])

def view_history():
    if not os.path.exists(HISTORY_FILE):
        print("\n📂 [System] No records found. Start your first prediction!")
        return
    print("\n" + "💎 STUDENT TRACKING HISTORY ".center(120, "="))
    print(f"{'DATE':<17} | {'NAME':<15} | {'AGE':<4} | {'STRESS':<6} | {'STATUS':<12} | {'AI ADVICE'}")
    print("-" * 120)
    with open(HISTORY_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Timestamp']:<17} | {row['Name']:<15} | {row['Age']:<4} | "
                  f"{row['stress_level']:<6} | {row['Status']:<12} | {row['Recommendation']}")
    print("=" * 120)
    input("\n[Press Enter to return to Menu]")

def get_valid_input(prompt, min_val=None, max_val=None, is_int=False):
    while True:
        try:
            val = input(prompt)
            value = int(val) if is_int else float(val)
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"   ❌ Value must be between {min_val} and {max_val}."); continue
            return value
        except ValueError: print("   ❌ Oops! Please enter a valid number.")

def train_model():
    if not os.path.exists(DATA_FILE):
        # Fallback if CSV is missing
        df = pd.DataFrame(np.random.randint(0,10, size=(200, 7)), columns=FEATURES + ["burnout"])
        df.to_csv(DATA_FILE, index=False)
    
    df = pd.read_csv(DATA_FILE)
    X, y = df[FEATURES], df["burnout"]
    # Using 'balanced' weights because burnout is often a minority class
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced').fit(X, y)
    return model

def predict_student(model):
    print("\n" + " 📋 STUDENT ASSESSMENT ".center(45, "◈"))
    name = input(" 👤 Name of Student: ").strip() or "Anonymous"
    age = get_valid_input(" 🎂 Age: ", 1, 120, True)
    
    print("\n" + " 📊 ENTER METRICS ".center(45, "-"))
    vals = [
        get_valid_input(" 📚 Daily Study Hours: ", 0, 24),
        get_valid_input(" 💤 Hours of Sleep: ", 0, 24),
        get_valid_input(" 📱 Social Media/Screen: ", 0, 24),
        get_valid_input(" 🤯 Stress Level (1-10): ", 1, 10, True),
        get_valid_input(" 🏃 Exercise Hours: ", 0, 24),
        get_valid_input(" ☕ Caffeine (Cups): ", 0, 20, True)
    ]
    
    print("\n" + " 🤖 AI IS THINKING ".center(45, "."))
    time.sleep(1.5)

    prob = model.predict_proba(pd.DataFrame([vals], columns=FEATURES))[0][1]
    res = 1 if prob > 0.55 else 0 # 0.55 threshold for safety
    sol = get_recommendation(vals)

    # --- Result UI ---
    print("\n" + "🌟 ANALYSIS COMPLETE 🌟".center(45))
    print(f" {'='*43}")
    print(f" 👤 PROFILE: {name} ({age} yrs)")
    
    if res == 1:
        print(f" 🚩 STATUS:  HIGH RISK OF BURNOUT")
        print(f" 📈 PROBABILITY: {prob:.1%}")
    else:
        print(f" ✅ STATUS:  HEALTHY BALANCE")
        print(f" 📈 PROBABILITY: {prob:.1%}")

    print(f"\n 💡 AI SUGGESTION: {sol}")
    print(f" {'='*43}")
    
    save_to_history(name, age, vals, prob, res, sol)
    input("\n[Record Saved] Press Enter to continue...")

def main():
    print("\n" + "🌈 WELCOME TO THE AI WELLNESS ASSISTANT 🌈".center(55))
    model = train_model()

    while True:
        print("\n" + " 🧭 MAIN MENU ".center(40, "━"))
        print(" [1] 🩺 Run New Prediction")
        print(" [2] 📂 View Track History")
        print(" [3] 🗑️  Clear All Records")
        print(" [4] 📊 View Data Insights")
        print(" [5] 🚪 Exit Application")
        
        choice = input("\n ⚡ Select an option: ").strip()
        
        if choice == '1': predict_student(model)
        elif choice == '2': view_history()
        elif choice == '3': clear_history()
        elif choice == '4':
            importances = model.feature_importances_
            print("\n" + " 🔍 WHAT DRIVES BURNOUT? ".center(40, "-"))
            for f, imp in sorted(zip(FEATURES, importances), key=lambda x: x[1], reverse=True):
                bar = "█" * int(imp * 40)
                print(f" {f.replace('_',' ').title():<15} {bar} {imp:.1%}")
            input("\n[Press Enter]")
        elif choice == '5':
            print("\n ✨ Remember: Rest is productive. Goodbye! ✨\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n 👋 Force closed. Stay healthy!")