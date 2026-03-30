import filesAndFolders
import tkinter as tk
from theme import Theme

stored_exitButton = None
stored_settingsButton = None

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

        #Removing the title bar and borders of the window to create a frameless window
        self.root.overrideredirect(True)

        #Creating the title bar and its components.
        self.title_bar = tk.Frame(self.canvas, bg="gray", relief='raised', bd=1)
        self.title_label = tk.Label(self.title_bar, text="Zenth", bg="gray", fg="white")

        self.text = tk.Text(master=self.canvas)


        #Initialize the theme from the theme module
        self.theme = Theme()

    def titleBar(self):
        '''
        Creating a Custom title bar for Zenith and appointing mouse buttons for it 
        '''
        self.title_bar.grid_columnconfigure(0, weight=1)
        self.title_bar.grid(row=0, column=0, columnspan=3, sticky='ew')

        self.title_label.grid(row=0, column=0, sticky='w', padx=10)

        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        self.title_label.bind("<Button-1>", self.start_move)
        self.title_label.bind("<B1-Motion>", self.do_move)

    #############################################TASKBAR BUTTONS###########################################################
    def exitButton(self):
        '''
        The exit button for the title bar
        '''
        btn_img = self.convertImage(file_path="./Assets/button_shrinked.png")
        
        exit_button = tk.Button(
            master=self.title_bar,
            image=btn_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            bg="gray",
            command=self.root.destroy
        )

        def on_enter(event):
            '''
            Visual signal for when the cursor hovers over the exit button.
            '''
            exit_button.config(relief="raised", bg="#505050")
        
        def on_leave(event):
            '''
            Resets the button when the cursor leaves the exit button.
            '''
            exit_button.config(relief="flat", bg="gray")
        
        #Appointing the on_enter and on_leave function to the exit button.
        exit_button.bind("<Enter>", on_enter)
        exit_button.bind("<Leave>", on_leave)
        
        #Saving the button in a local variable so python doesn't dump it.
        exit_button.image = btn_img 
        
        exit_button.grid(row=0, column=1, sticky='w', padx=5, pady=5)
    
    def settingsButton(self):
        '''
        Settings button that leads to the theme window.
        '''
        btn_image = self.convertImage(file_path="./Assets/gear_shrinked.png")
        sButton = tk.Button(master=self.canvas, 
                            image=btn_image,
                            relief="flat",
                            borderwidth=0,
                            highlightthickness=0,
                            bg="gray",
                            command=self.openSettings)
        sButton.image = btn_image
        sButton.grid(row=4, column=2, padx=5, pady=5)

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
        #Changing the theme of canvas
        self.canvas.configure(bg=self.theme.themes[selectedTheme]["background"])
        #Changing the theme of the title bar and its components.
        self.title_bar.config(bg=self.theme.themes[selectedTheme]["background"])
        self.title_label.config(fg=self.theme.themes[selectedTheme]["foreground"], bg=self.theme.themes[selectedTheme]['background'])

        self.text.config(fg=self.theme.themes[selectedTheme]["foreground"], bg=self.theme.themes[selectedTheme]["background"])
        

    #############################################IMAGE CONVERSION###########################################################
    def convertImage(self, file_path):
        '''
        Converts a normal image into a PhotoImage so it can be used by tkinter.
        '''
        converted_photo = tk.PhotoImage(file=file_path)
        return converted_photo

    #############################################SHOW FILES###########################################################
    def showFiles(self):
        self.text.grid(column=1, row=3)
        self.text.config(borderwidth=0)
        self.text.insert("1.0", filesAndFolders.showFiles())
    
    #############################################SHOW FILES###########################################################
    def openSettings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x400")
        
    
