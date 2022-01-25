from pathlib import Path

import panel as pn

from models.pages import Page

DIR_PATH = Path(__file__).parent
STATS_FILE = 'statistics.md'

statistics = Path(DIR_PATH, STATS_FILE).read_text(encoding='utf8')


class StatisticsPage(Page):

    def __init__(self):
        super().__init__()
        self.pane = pn.pane.Markdown(statistics, width=1000)
        self.button = pn.widgets.Button(name='Statistics')

    def get_contents(self):
        return self.pane, self.button
