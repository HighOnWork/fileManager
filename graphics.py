import tkinter as tk
from theme import Theme

width = 800
height = 600
class FileManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}+100+100")

        #Variables to store mouse position
        self.offset_x = 0
        self.offset_y = 0

        #Giving weight to the rows and columns of the root window to make the canvas expand to fill the window
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        #Creating a canvas to hold the title bar and the theme menu, and making it expand to fill the window
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.grid(column=0, row=0, sticky='nsew')

        #Giving weight to the canvas so that the elements inside it can be moved freely
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_columnconfigure(1, weight=1)
        self.canvas.grid_rowconfigure(3, weight=1)

        self.root.title("Zenith")

        # Removing the title bar and borders of the window to create a frameless window
        self.root.overrideredirect(True)

        ##################################TEMP#################################
        tk.Button(self.canvas,
                  text="Exit",
                  command=self.root.destroy).grid(row=3, column=2, sticky='s', padx=10, pady=10)
        #######################################################################

        #Initialize the theme from the theme module
        self.theme = Theme()

    def titleBar(self):
        '''
        Creating a Custom title bar for Zenith and appointing mouse buttons for it 
        '''
        title_bar = tk.Frame(self.canvas, bg="gray", relief='raised', bd=1)
        title_bar.grid_columnconfigure(0, weight=1)
        title_bar.grid(row=0, column=0, columnspan=3, sticky='ew')

        title_label = tk.Label(title_bar, text="Zenth", bg="gray", fg="white")
        title_label.grid(row=0, column=0, sticky='w', padx=10)

        title_bar.bind("<Button-1>", self.start_move)
        title_bar.bind("<B1-Motion>", self.do_move)
        title_label.bind("<Button-1>", self.start_move)
        title_label.bind("<B1-Motion>", self.do_move)
    
    def settingsButton(self):
        '''
        Settings button that leads to the theme window.
        '''
        sButton = tk.Button(self.canvas, image="./Assets/gear.png").grid(row=2, column=2)

    ##########################################MOVING THE TASKBAR AROUND#####################################################

    def start_move(self, event):
        '''
        Records the distance from the screen to the window.
        '''
        self.offset_x = event.x_root - self.root.winfo_x()
        self.offset_y = event.y_root - self.root.winfo_y()

    def do_move(self, event):
        '''
        Calculates new window position.
        '''
        new_x = event.x_root - self.offset_x
        new_y = event.y_root - self.offset_y
        self.root.geometry(f"+{new_x}+{new_y}")
        self.root.update_idletasks()


    #############################################THEME SETTINGS###########################################################
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

    
    
