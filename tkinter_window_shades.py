from tkinter import Tk, Scale

# Create the main window
win = Tk()
win.configure(background='black')
win.wm_attributes("-alpha", .65)
win.geometry("700x350")

# Function to change the opacity of the main window
def change_opacity(value):
    win.wm_attributes("-alpha", float(value))

# Create a new window for the scale widget
scale_win = Tk()
scale_win.geometry("+0+500")  # Position the window at the bottom left of the screen

# Create a new Scale widget in the scale window
opacity_scale = Scale(scale_win, from_=0.0, to=1.0, resolution=0.01, orient="vertical", command=change_opacity)
opacity_scale.set(.65)  # Set the initial value
opacity_scale.pack()

win.mainloop()