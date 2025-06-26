

import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Animated GIF Background with Fade Transitions")
root.geometry("1920x1080")

# Load the GIF image using Pillow (PIL)
gif_image = Image.open("cric_ninja.png")

# Create a PhotoImage object from the first frame of the animated GIF
photo = ImageTk.PhotoImage(gif_image)

# Create a label to display the animated GIF with opacity
class AnimatedLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.alpha = 0.0
        self.delta = 0.01
        self.animate_fade_in()

    def animate_fade_in(self):
        self.alpha += self.delta
        self.update_alpha()
        if self.alpha < 1.0:
            root.after(20, self.animate_fade_in)
        else:
            root.after(3000, self.animate_fade_out)  # Start fade-out after 3 seconds

    def animate_fade_out(self):
        self.alpha -= self.delta
        self.update_alpha()
        if self.alpha > 0.0:
            root.after(20, self.animate_fade_out)
        else:
            root.destroy()  # Close the window after fade-out

    def update_alpha(self):
        alpha = int(255 * self.alpha)
        image = gif_image.convert("RGBA")
        image.putalpha(alpha)
        self.photo = ImageTk.PhotoImage(image)
        self.configure(image=self.photo)

bg_label = AnimatedLabel(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# You can add other widgets on top of the animated GIF background
label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=0)

# Start the Tkinter main loop
root.mainloop()
