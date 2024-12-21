import tkinter as tk
from tkinter import messagebox
import pyttsx3

# إعداد المحرك الصوتي
engine = pyttsx3.init()

# الدالة التي تشغل النص
def play_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("تنبيه", "الرجاء إدخال نص.")

# الدالة للخروج من البرنامج
def exit_program():
    window.destroy()

# الدالة لمسح النص من حقل الإدخال
def set_settings():
    text_input.delete("1.0", tk.END)  # مسح النص بالكامل من حقل الإدخال

# إنشاء نافذة البرنامج
window = tk.Tk()
window.title("Text-to-Speech")
window.geometry("500x400")
window.configure(bg="#f0f0f0")

# عنوان
title_label = tk.Label(window, text="Text-to-Speech", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

# إدخال النص
text_input = tk.Text(window, height=8, width=50, font=("Arial", 12), bg="#ffffff", fg="#000000", bd=2, relief="groove")
text_input.pack(pady=15)

# الأزرار
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

play_button = tk.Button(button_frame, text="Play", command=play_text, width=12, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
play_button.grid(row=0, column=0, padx=15, pady=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_program, width=12, font=("Arial", 10, "bold"), bg="#f44336", fg="white")
exit_button.grid(row=0, column=1, padx=15, pady=10)

set_button = tk.Button(button_frame, text="Set", command=set_settings, width=12, font=("Arial", 10, "bold"), bg="#2196F3", fg="white")
set_button.grid(row=0, column=2, padx=15, pady=10)

# تشغيل البرنامج
window.mainloop()
