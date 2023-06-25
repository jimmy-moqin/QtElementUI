import os

import sass

WidgetName = {
    "button": "buttons.scss",
}


class ThemeManager:

    def __init__(self, theme_mode, widget_name):
        self.theme_mode = theme_mode

        if self.theme_mode == "light":
            self.THEME = "light"
            # load all scss files in resource/qss/light
            self._load_theme("light", widget_name)
        elif self.theme_mode == "dark":
            self.THEME = "dark"
            # load all scss files in resource/qss/dark
            self._load_theme("dark", widget_name)

    def _load_theme(self,theme_mode, widget_name):
        # load all scss files in resource/qss/light
        for file in os.listdir(f"resource/qss/{theme_mode}"):
            if (file.endswith(".scss")) and (file == WidgetName[widget_name]):
                with open(f"resource/qss/{theme_mode}/{file}") as f:
                    self.qss = sass.compile(string=f.read())
    def apply_theme(self,widget):
        widget.setStyleSheet(self.qss)
