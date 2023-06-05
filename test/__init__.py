import tkinter as tk

root = tk.Tk()
version = root.tk.call('info', 'patchlevel')
print(f"A versão do Tkinter instalada é: {version}")

root.mainloop()
