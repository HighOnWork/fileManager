from graphics import FileManagerApp

def main():
    app = FileManagerApp()
    app.titleBar()
    #Generating buttons
    app.exitButton()
    app.settingsButton()
    #Listing files
    app.showFiles()
    # app.settingsButton()
    choosenTheme = app.themeMenu()
    app.changingTheme(choosenTheme)
    app.applyingTheme(choosenTheme)

    app.root.mainloop()

if __name__ == '__main__':
    main()
    