import tkinter as tk
from tkinter.filedialog import askopenfilename

window = tk.Tk()
filename = askopenfilename()
window.mainloop()