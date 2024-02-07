from tkinter import Tk, Label, BOTTOM

# Create the main window
win = Tk()
win.configure(background='black')
opacity_start = 0.65

win.wm_attributes("-alpha", .65)
win.geometry("700x350")

# Create a label to display the opacity
opacity_label = Label(win, text=f"<<left arrow--Opacity: {opacity_start * 100:.0f}--right arrow>>%", bg="grey")
opacity_label.pack(side=BOTTOM)

# Function to change the opacity of the main window
def change_opacity(value):
    current_opacity = float(win.wm_attributes("-alpha"))
    new_opacity = current_opacity + value
    new_opacity = min(max(new_opacity, 0.0), 1.0)  # Ensure the opacity stays between 0.0 and 1.0
    win.wm_attributes("-alpha", new_opacity)
    opacity_label.config(text=f"<<left arrow--Opacity: {new_opacity * 100:.0f}%--right arrow>>")  # Update the label text

# Bind the left arrow key to a function that decreases the opacity
win.bind('<Left>', lambda event: change_opacity(-0.01))

# Bind the right arrow key to a function that increases the opacity
win.bind('<Right>', lambda event: change_opacity(0.01))

win.mainloop()