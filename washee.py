import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import sys

if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

root = tk.Tk()
root.title("how do i get him off")

image_path = "washee.png"
img = Image.open(image_path)
img = img.convert("RGBA")

image_tk = ImageTk.PhotoImage(img)

width, height = img.size
root.geometry(f"{width}x{height}+100+100")

root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "blue")

canvas = tk.Canvas(root, width=width, height=height, bg="blue", highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, anchor="nw", image=image_tk)

root.mainloop()

print("how do i get him off")