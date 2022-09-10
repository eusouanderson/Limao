from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.contents = StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())


root = Tk()
root.geometry('290x250+400+100')
root.title('Ola')
myapp = App(root)
myapp.master.title('Ola ')



myapp.mainloop()
