from dashboard import Dashboard
from dashboard.pages import HomePage, DataUnderstandingPage, VisualizationPage

# pages
home_page = HomePage()
understanding_page = DataUnderstandingPage()
visualization_page = VisualizationPage()

# page panes and buttons
home_pane, home_btn = home_page.get_contents()
understanding_pane, understanding_btn = understanding_page.get_contents()
vis_pane, vis_btn = visualization_page.get_contents()

panes = {
    'home': home_pane,
    'understanding': understanding_pane,
    'visualization': vis_pane
}

btns = {
    'home': home_btn,
    'understanding': understanding_btn,
    'visualization': vis_btn
}

if __name__ == '__main__':
    dashboard = Dashboard(title='Disease and Life Expectancy',
                          panes=panes, btns=btns, modal={}, home_pane='visualization')
    dashboard.serve(50000)
