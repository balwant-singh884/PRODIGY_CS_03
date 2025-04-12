import tkinter as tk
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add a lowercase letter")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add a number")

    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
    else:
        feedback.append("❌ Add a special character")

    return strength, feedback

def evaluate_password():
    password = entry.get()
    strength, feedback = check_password_strength(password)
    
    # Show entered password
    entered_label.config(text=f"Entered Password: {password}")

    # Display strength
    if strength <= 2:
        result.config(text="Strength: Weak 🔴", fg="red")
    elif strength == 3 or strength == 4:
        result.config(text="Strength: Medium 🟡", fg="orange")
    else:
        result.config(text="Strength: Strong 🟢", fg="green")

    # Show suggestions
    tips.config(text="\n".join(feedback) if feedback else "✅ Good job!")

# GUI setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("420x320")
root.config(padx=20, pady=20)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack()
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root, text="Check Password", command=evaluate_password, font=("Arial", 12)).pack(pady=10)

entered_label = tk.Label(root, text="", font=("Arial", 11), fg="blue")
entered_label.pack()

result = tk.Label(root, text="", font=("Arial", 14, "bold"))
result.pack()

tips = tk.Label(root, text="", font=("Arial", 10), fg="gray", justify="left")
tips.pack(pady=10)

root.mainloop()
