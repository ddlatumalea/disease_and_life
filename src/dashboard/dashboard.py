import panel as pn

pn.extension('plotly')


class Dashboard:
    """ Returns an interactive dashboard for data visualization.

    Keyword arguments:
        title -- the title of the dashboard.
        panes -- a dictionary of panel panes and identifiers.
        btns -- a dictionary of panel buttons and identifiers.
        home_pane -- the key of the pane that is shown by default.
    """

    def __init__(self, title: str, panes: dict, modal: dict, btns: dict, home_pane: str) -> None:
        if home_pane not in panes:
            raise ValueError('Home pane must be in panes.')
        if len(panes) < 1:
            raise ValueError('Expects at least one pane.')
        if len(modal) > 1:
            raise ValueError('Only 1 modal is allowed.')

        # accent_base_color='#xxxxxx' changes the accent, default is pink
        self.base = pn.template.FastListTemplate(title=title,)
        self.panes = panes
        self.btns = btns
        self.modals = modal


        # create a row and append it to the main panel of the template
        self.row = pn.Row(self.panes[home_pane])
        self.base.main.append(
            pn.Column(
                self.row
            )
        )

        # assign callbacks to the buttons and append them to the sidebar
        if len(self.btns) > 0:
            for k in self.btns.keys():
                self.btns[k].on_click(self.get_callback(k))

            self.base.sidebar.extend([btn for btn in self.btns.values()])

        if len(self.modals) > 0:
            self.base.modal.extend([modal for modal in self.modals.values()])

    def get_callback(self, key: str) -> pn.Pane:
        """Callbacks that can alter the dashboard."""

        def change_pane(event):
            self.row[0] = self.panes[key]

        def open_modal(event):
            self.base.open_modal()

        collection = {
            'home': change_pane,
            'understanding': change_pane,
            'visualization': change_pane
        }

        return collection[key]

    def serve(self, port: int):
        self.base.show(port=port)
