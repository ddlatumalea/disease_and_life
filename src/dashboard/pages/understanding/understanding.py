from pathlib import Path

import panel as pn

from models.pages import Page

DIR_PATH = Path(__file__).parent
PDF_FILE = 'Data understanding.pdf'

pdf_path = Path(DIR_PATH, PDF_FILE)


class DataUnderstandingPage(Page):

    def __init__(self):
        super().__init__()
        self.pane = pn.pane.PDF(pdf_path, height=1000)
        self.button = pn.widgets.Button(name='Data Understanding')

    def get_contents(self):
        return self.pane, self.button
