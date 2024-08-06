import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Scoring system
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    # Strength feedback
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Feedback message
    feedback = []
    if not length_criteria:
        feedback.append("Increase the length to at least 8 characters.")
    if not lowercase_criteria:
        feedback.append("Add lowercase letters.")
    if not uppercase_criteria:
        feedback.append("Add uppercase letters.")
    if not number_criteria:
        feedback.append("Add numbers.")
    if not special_char_criteria:
        feedback.append("Add special characters (e.g., !, @, #, $, %, etc.).")

    return strength, feedback

def check_password():
    password = password_entry.get()
    strength, feedback = password_strength(password)

    result_text = f"Password Strength: {strength}\n"
    if feedback:
        result_text += "Feedback to improve your password:\n"
        for suggestion in feedback:
            result_text += f"- {suggestion}\n"
    else:
        result_text += "Your password is very strong!"

    messagebox.showinfo("Password Strength Result", result_text)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the password entry widget
tk.Label(root, text="Enter a password to check its strength:").pack(pady=10)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=10)

# Create and place the check button
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
