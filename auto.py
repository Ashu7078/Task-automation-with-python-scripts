import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Directory does not exist!")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            category = "Others"
            
            for cat, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category = cat
                    break
            
            category_path = os.path.join(directory, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            
            shutil.move(file_path, os.path.join(category_path, filename))
    
    messagebox.showinfo("Success", "File organization complete!")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        organize_files(folder_path)

def create_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("400x200")
    root.configure(bg="#333333")
    
    label = tk.Label(root, text="Select a folder to organize", bg="#333333", fg="white", font=("Arial", 12))
    label.pack(pady=10)
    
    select_button = tk.Button(root, text="Select Folder", command=select_folder, bg="#555555", fg="white", font=("Arial", 12, "bold"))
    select_button.pack(pady=5)
    
    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#ff5555", fg="white", font=("Arial", 12, "bold"))
    exit_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
