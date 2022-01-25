from pathlib import Path

import panel as pn

from models.pages import Page

DIR_PATH = Path(__file__).parent
HOME_FILE = 'home.md'

home = Path(DIR_PATH, HOME_FILE).read_text(encoding='utf8')


class HomePage(Page):

    def __init__(self):
        super().__init__()
        self.pane = pn.pane.Markdown(home, width=1000)
        self.button = pn.widgets.Button(name='Home')

    def get_contents(self):
        return self.pane, self.button
