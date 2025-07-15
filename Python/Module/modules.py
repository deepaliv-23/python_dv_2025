
# JSON Module
import json  
data = {
    "name": "Jonny",
    "age": 30,
    "is_student": True,
    "courses": ["Web Dev", "CP"]
}
json_string = json.dumps(data, indent=4)
print(json_string)

# thinker module
import tkinter as tk  
def on_button_click():  
    label.config(text="Hello, Geeks!")

root = tk.Tk()
root.title("Tkinter Example")  
label = tk.Label(root, text="Click the button below")  
label.pack(pady=40)  
button = tk.Button(root, text="Click Me", command=on_button_click) 
button.pack(pady=40)  
root.mainloop()

# random number
import random  
num = random.randint(1, 10)
print(f"Random integer between 1 and 10: {num}")
fruits = ["Java", "C", "C++", "Python"]
chosen_fruit = random.choice(fruits)
print(f"Randomly chosen language: {chosen_fruit}")

# math module
import math
sqrt_val = math.sqrt(64)
pi_const = math.pi
print(sqrt_val)
print(pi_const)

# datetime module
import datetime
date_today = datetime.date.today()
time_now = datetime.datetime.now().time()
print(date_today)
print(time_now)

# os module
import os
directory = os.getcwd()
print(directory)

# sys module
import sys
print("Python version:", sys.version)
print("Command line arguments:", sys.argv)
sys.exit(1)

# SYS module
import re
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"

text = "Contact us at info@example.com and support@example.org for more details."
match = re.search(pattern, text)
if match:
    print("First found email:", match.group())

emails = re.findall(pattern, text)
print("All found emails:", emails)

# hashlib Module
import hashlib
message = "Hello, World!"
hashed = hashlib.sha256(message.encode()).hexdigest()
print(hashed)

# calendar module
import calendar
cal_october = calendar.month(2023, 10)
print(cal_october)

# heapq module
import heapq
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

heapq.heapify(numbers)
heapq.heappush(numbers, 7)
print(heapq.heappop(numbers)) 
print(heapq.heappushpop(numbers, 8)) 
print(heapq.nlargest(3, numbers))  
print(heapq.nsmallest(3, numbers))
