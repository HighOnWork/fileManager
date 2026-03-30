from graphics import FileManagerApp

def main():
    app = FileManagerApp()
    app.titleBar()
    app.exitButton()
    app.showFiles()
    # app.settingsButton()
    choosenTheme = app.themeMenu()
    app.changingTheme(choosenTheme)
    app.applyingTheme(choosenTheme)
    #Lists the files in the current directory and prints them to the console
    app.root.mainloop()

if __name__ == '__main__':
    main()
    