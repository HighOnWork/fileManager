import tkinter as tk
from theme import Theme

width = 800
height = 600
class FileManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)

        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.grid(column=0, row=0, sticky='nsew', columnspan=2)

        self.root.title("Zenth")
        # Removing the title bar and borders of the window to create a frameless window
        self.root.overrideredirect(True)

        ##################################TEMP#################################
        tk.Button(self.canvas,
                  text="Exit",
                  command=self.root.destroy).grid(row=3, column=2)
        #######################################################################

        #Initialize the theme from the theme module
        self.theme = Theme()

    def titleBar(self):
        title_bar = tk.Frame(self.canvas, bg="gray", relief='raised', bd=1)
        title_bar.grid(row=0, column=0, sticky='ew')

        title_label = tk.Label(title_bar, text="Zenth", bg="gray", fg="white")
        title_label.grid(row=0, column=0)


    def themeMenu(self):
        '''
        Creates a dropdown menu for selecting themes and returns the selected theme as a StringVar.
        '''
        optionSelected = tk.StringVar(value=self.theme.defaultTheme)
        tk.OptionMenu(self.canvas, optionSelected, *self.theme.themes.keys()).grid(row=1, column=0)
        return optionSelected

    def applyingTheme(self, theme):
        '''
        Button for applying the selected theme.
        '''
        tk.Button(self.canvas,
                  text="Apply",
                  command=lambda: self.changingTheme(theme=theme)
                  ).grid(row=2, column=0)

    def changingTheme(self, theme):
        '''
        Ran once at the start and then when the "Apply" button is clicked. Changes the app's theme based on the selected theme from the dropdown menu.
        '''
        selectedTheme = theme.get().capitalize()
        self.canvas.configure(bg=self.theme.themes[selectedTheme]["background"])

    
