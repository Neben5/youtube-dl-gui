import tkFileDialog
from Tkinter import mainloop, Tk, Label, StringVar, Entry, Button
import extractor
import os.path

# Queries user for destination path
def selectDestination(destination):
    filename = tkFileDialog.asksaveasfilename(initialdir="/", title="Select file",
                                              filetypes=(("*.mp3", "*.mp4"), ("all files", "*.*")))
    try:
        destination.insert(0, filename)
    except:
        pass


class gui:
    bg = '#252429'
    fontColor = '#31d0a7'
    textBoxColor = '#45434b'

    def __init__(self):
        self.root = self.initializeFrame()
        self.topLabel()
        self.target = self.targetTextBox()
        self.destination = self.destinationTextBox()

        self.startButton()
        mainloop()

    # Sets up frame
    def initializeFrame(self):
        path = os.path.dirname(os.path.realpath(__file__))
        root = Tk()
        root.resizable(False, False)
        root.title("Pirateer")
        try:
            root.iconbitmap(r"{0}\icon.ico".format(path))
        except:
            pass
        root.configure(background=self.bg)

        return root

    # topLabel set to row 0
    def topLabel(self):
        test = Label(self.root, text="Pirateer", fg=self.fontColor, bg=self.bg)
        test.grid(row=0, sticky="NESW", columnspan=10)
        return test

    # target text set to row 1
    def targetTextBox(self):
        targetText = Label(self.root, text="Target URL", bg=self.bg, fg=self.fontColor)
        targetText.grid(row=1, column=0)
        targetVar = StringVar()
        target = Entry(self.root, textvariable=targetVar, bg=self.textBoxColor, fg=self.fontColor)
        target.grid(row=1, column=1)
        return targetVar

    # destination set to row 2
    def destinationTextBox(self):
        destinationText = Label(self.root, text="Destination", bg=self.bg, fg=self.fontColor)
        destinationText.grid(row=2, column=0)
        destinationVar = StringVar()
        destination = Entry(self.root, textvariable=destinationVar, bg=self.textBoxColor, fg=self.fontColor)
        destination.grid(row=2, column=1)
        selectionButton = Button(self.root, text="Select", command=lambda: selectDestination(destination),
                                 bg=self.textBoxColor, fg=self.fontColor)
        selectionButton.grid(row=2, column=2, padx=3)
        return destinationVar

    def startButton(self):
        button = Button(self.root, text="Start", bg=self.bg, fg=self.fontColor, command=lambda: self.start())
        button.grid(row=3, sticky="NESW", columnspan=10)

    def start(self):
        extractor.downloader(self.destination, self.target)
        pass


if __name__ == '__main__':
    gui()
