import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

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

class PasswordStrengthApp(App):
    def build(self):
        self.window = BoxLayout(orientation='vertical')
        
        self.label = Label(
            text="Enter a password to check its strength:",
            font_size=18,
            halign="center",
            valign="middle"
        )
        self.window.add_widget(self.label)
        
        self.password_input = TextInput(
            multiline=False,
            password=True,
            font_size=24,
            halign="center"
        )
        self.window.add_widget(self.password_input)
        
        self.button = Button(
            text="Check Strength",
            size_hint=(1, 0.5),
            font_size=18,
            on_press=self.check_password_strength
        )
        self.window.add_widget(self.button)
        
        self.result_label = Label(
            text="",
            font_size=18,
            halign="center",
            valign="middle"
        )
        self.window.add_widget(self.result_label)
        
        return self.window

    def check_password_strength(self, instance):
        password = self.password_input.text
        strength, feedback = password_strength(password)
        
        self.result_label.text = f"Password Strength: {strength}"
        if feedback:
            self.result_label.text += "\nFeedback to improve your password:"
            for suggestion in feedback:
                self.result_label.text += f"\n- {suggestion}"
        else:
            self.result_label.text += "\nYour password is very strong!"

if __name__ == "__main__":
    PasswordStrengthApp().run()
