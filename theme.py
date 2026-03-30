class Theme:
    def __init__(self):

        self.defaultTheme = "Dark"

        self.themes = {
            "Dark": {
                "foreground": "#FFFFFF",
                "background": "#000000"
            },
            "Light": {
                "foreground": "#000000",
                "background": "#FFFFFF"
            },
            "Gruvbox": {
                "foreground": "#EBDBB2",
                "background": "#282828"
            },
            "Plum": {
                "foreground": "#E5C1FF",
                "background": "#2D1B4E"
            },
            "Solarized dark": {
                "foreground": "#839496",
                "background": "#002B36"
            },
            "Solarized light": {
                "foreground": "#586E75",
                "background": "#FDF6E3"
            },
            "Monokai": {
                "foreground": "#F8F8F2",
                "background": "#272822"
            },
            "Nord": {
                "foreground": "#D8DEE9",
                "background": "#2E3440" 
            },
            "Dracula": {
                "foreground": "#F8F8F2",
                "background": "#282A36"
            },
            "Mint": {
                "foreground": "#2E3440",
                "background": "#D8EEEB"
            },
            "Twilight": {
                "foreground": "#E4E4E4",
                "background": "#141414"
            }
        }
