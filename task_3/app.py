import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
import threading
import time

def update_loading_circle(canvas, circle, angle):
    # Update the loading circle to show progress
    canvas.itemconfig(circle, extent=angle)
    angle += 5
    if angle > 360:
        angle = 0
    return angle

def show_loading():
    global loading
    loading = True
    loading_label.grid()
    loading_canvas.grid()
    angle = 0
    while loading:
        angle = update_loading_circle(loading_canvas, loading_circle, angle)
        app.update_idletasks()
        time.sleep(0.05)

def hide_loading():
    global loading
    loading = False
    loading_label.grid_remove()
    loading_canvas.grid_remove()

def generate_image_thread(description):
    pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
    try:
        # Generate the image
        image = pipe(description).images[0]
        image.save("output.png")  # Save the generated image to a file
    except Exception as e:
        hide_loading()
        messagebox.showerror("Generation Error", str(e))
        return

    try:
        # Open the saved image and convert it to a format Tkinter can use
        pil_image = Image.open("output.png")
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # Update the img_label with the new image
        img_label.config(image=tk_image)
        img_label.image = tk_image
        img_label.config(text="")
    except Exception as e:
        hide_loading()
        messagebox.showerror("Display Error", str(e))
        return

    hide_loading()

def generate_image():
    description = description_entry.get()  # Get the text from the entry widget
    if description == "":
        messagebox.showerror("Input Error", "Description cannot be empty.")
        return

    threading.Thread(target=show_loading).start()
    threading.Thread(target=generate_image_thread, args=(description,)).start()

# Create the interface
app = tk.Tk()
app.title("Tkinter Application UI")
app.config(bg="#ff9800")

# Center the window
window_width = 600
window_height = 400
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
app.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create a frame for content with padding
frame = tk.Frame(app, bg="#ff9800", padx=20, pady=20)
frame.grid(sticky="nsew")

# Make the frame expandable
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Description label and entry
description_label = tk.Label(frame, text="Description:", bg="#ff9800", font=("Arial", 14))
description_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
description_entry = ttk.Entry(frame, font=("Arial", 14))
description_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Generate button
generate_button = tk.Button(frame, text="Generate Image", command=generate_image, bg="#6c757d", fg="white", font=("Arial", 14))
generate_button.grid(row=0, column=2, padx=10, pady=10)

# Image display frame and label
image_frame = tk.Frame(frame, bg="gray", width=400, height=300)
image_frame.grid(row=1, column=0, columnspan=3, pady=20, sticky="nsew")
img_label = tk.Label(image_frame, text="L'image sera générée ici", bg="gray", font=("Arial", 14))
img_label.pack(expand=True)

# Make the image frame expandable
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Loading spinner (circular)
loading_canvas = tk.Canvas(frame, width=50, height=50, bg="#ff9800", highlightthickness=0)
loading_circle = loading_canvas.create_arc((10, 10, 40, 40), start=0, extent=0, outline="white", style="arc", width=5)

# Loading message
loading_label = tk.Label(frame, text="Loading...", bg="#ff9800", fg="white", font=("Arial", 14))

# Hide the loading elements initially
loading_label.grid(row=2, column=0, columnspan=3, pady=10)
loading_canvas.grid(row=3, column=0, columnspan=3, pady=10)
loading_label.grid_remove()
loading_canvas.grid_remove()

# Make widgets responsive
for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

# Start the app
app.mainloop()
