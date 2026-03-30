from graphics import FileManagerApp

def main():
    app = FileManagerApp()
    app.titleBar(app.title_bar, app.title_label)
    #Generating buttons for zenith title bar
    app.exitButton(app.title_bar)
    app.settingsButton()
    #Generating buttons for the settings window

    #Listing files
    app.showFiles()
    # app.settingsButton()
    choosenTheme = app.themeMenu()
    app.changingTheme(choosenTheme)
    app.applyingTheme(choosenTheme)

    app.root.mainloop()

if __name__ == '__main__':
    main()
    