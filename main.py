import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Define the function that runs when the button is clicked
def on_click():
    engine.say("Hello")
    engine.runAndWait()


# Set up the main GUI window
root = tk.Tk()
root.title("Voice Assistant Greeting App")

# Create and pack the button
greeting = tk.Button(root, text="Greeter", command=on_click, padx=5, pady=5)
greeting.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
