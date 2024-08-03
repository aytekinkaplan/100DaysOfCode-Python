import tkinter as tk

root = tk.Tk()
root.title("Basit GUI")

label = tk.Label(root, text="Merhaba, Dünya!")
label.pack()

button = tk.Button(root, text="Tıkla", command=root.quit)
button.pack()

root.mainloop()