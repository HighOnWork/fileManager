import os
from graphics import FileManagerApp

def main():
    app = FileManagerApp()
    app.titleBar()
    choosenTheme = app.themeMenu()
    app.changingTheme(choosenTheme)
    app.applyingTheme(choosenTheme)
    #Lists the files in the current directory and prints them to the console
    names = os.listdir('.')
    print(f"The files in the current directory are: {names}")
    app.root.mainloop()

if __name__ == '__main__':
    main()
    