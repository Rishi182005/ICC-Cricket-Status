import tkinter as tk
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to fetch and display website content in the GUI
def fetch_and_display_website_content():
    url = website_url.get()
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        # Extract and display the content in a text widget
        content_text.delete(1.0, tk.END)
        content_text.insert(tk.END, str(soup))

# Create a GUI window
root = tk.Tk()
root.title("Website Content Display")

# Label and Entry to enter the website URL
website_url_label = tk.Label(root, text="Enter Website URL:")
website_url_label.pack()
website_url = tk.Entry(root)
website_url.pack()

# Button to fetch and display content
fetch_button = tk.Button(root, text="Fetch Website Content", command=fetch_and_display_website_content)
fetch_button.pack()

# Text widget to display the website content
content_text = tk.Text(root)
content_text.pack()

root.mainloop()
