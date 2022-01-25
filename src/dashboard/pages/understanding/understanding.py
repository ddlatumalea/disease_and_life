from pathlib import Path

import panel as pn

from models.pages import Page

DIR_PATH = Path(__file__).parent
PDF_DOCU_FILE = 'dataset-documentation.pdf'
PDF_UNDERSTANDING_FILE = 'data understanding.pdf'

pdf_docu_path = Path(DIR_PATH, PDF_DOCU_FILE)
pdf_understanding_path = Path(DIR_PATH, PDF_UNDERSTANDING_FILE)


class DataUnderstandingPage(Page):

    def __init__(self):
        super().__init__()
        self.pane = pn.Tabs(('Findings', pn.pane.PDF(pdf_understanding_path, width=1000, height=1000)),
                            ('Document', pn.pane.PDF(pdf_docu_path, width=1000, height=1000)))
        self.button = pn.widgets.Button(name='Data Understanding')

    def get_contents(self):
        return self.pane, self.button
