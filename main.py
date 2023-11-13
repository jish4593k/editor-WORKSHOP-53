import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class AdvancedTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Text Editor")
        self.text_pad = scrolledtext.ScrolledText(root, width=100, height=30, wrap=tk.WORD)
        self.text_pad.pack(expand=True, fill='both')
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        analysis_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Text Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="Word Count", command=self.word_count_analysis)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=self.about)

    def new_file(self):
        self.text_pad.delete('1.0', tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_pad.delete('1.0', tk.END)
                self.text_pad.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_pad.get('1.0', tk.END))

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def about(self):
        messagebox.showinfo("About", "Advanced Text Editor\nCreated by: Your Name")

    def word_count_analysis(self):
        text_content = self.text_pad.get('1.0', tk.END)
        words = re.findall(r'\b\w+\b', text_content)
        word_count = len(words)

        messagebox.showinfo("Word Count Analysis", f"Total words: {word_count}")

        # Plot word frequency distribution
        word_freq = pd.Series(words).value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=word_freq.index[:10], y=word_freq.values[:10])
        plt.title("Top 10 Word Frequency")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45, ha='right')
        plt.show()

if __name__ == '__main__':
    root = tk.Tk()
    editor = AdvancedTextEditor(root)
    root.mainloop()
