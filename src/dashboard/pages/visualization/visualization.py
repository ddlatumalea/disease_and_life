from pathlib import Path

import panel as pn
import pandas as pd
import plotly.express as px

from models.pages import Page
from models.utils.paths import get_prepared_data_path, get_standardized_data_file
from dashboard.widgets import heatmap

PREPARED_DATA_DIR = get_prepared_data_path()
PREPARED_DATA_FILE = get_standardized_data_file()

COLUMNS = ['non-communicable chronic disease [deaths]',
           'cancer [deaths]', 'cardiovascular disease [deaths]',
           'diabetes mellitus [deaths]', 'chronic respiratory diseases [deaths]',
           'diseases of digestive system [deaths]',
           'life expectancy [age]']


def get_correlation_heatmap(df, columns):
    corr = df[columns].corr()

    z = corr.values.round(decimals=2)
    x = corr.index
    y = corr.index

    return heatmap(z, x, y, labels=dict(color='Correlation'))


def get_line_plot(df, x_col, y_col, index, title, width=500):
    if width is None:
        fig = px.line(df, x=x_col, y=y_col, color=index, title=title)
        return pn.pane.Plotly(fig)
    else:
        fig = px.line(df, x=x_col, y=y_col, color=index, title=title, width=width)
        return pn.pane.Plotly(fig)


data = pd.read_csv(Path(PREPARED_DATA_DIR, PREPARED_DATA_FILE))
df = data[data['sex'] == 3]


class VisualizationPage(Page):

    def __init__(self):
        super().__init__()
        self.df = df
        self.checkbutton = pn.widgets.CheckButtonGroup(name='Countries', value=['Netherlands'],
                                                       options=['Netherlands', 'Japan', 'Canada'])

        self.pane = pn.Column(self.checkbutton, self.get_plot(self.checkbutton))
        self.button = pn.widgets.Button(name='Visualization')

        self.checkbutton.param.watch(self.update, 'value')

    def get_plot(self, checkbutton):
        gspec = pn.GridSpec(ncols=2, nrows=4, width=1200, height=1800)

        selection = df.loc[df['country'].isin(checkbutton.value)]

        # life expectancy plot
        life_exp_plot = pn.pane.Plotly(
            px.line(selection, x='year', y='life expectancy [age]', color='country', title='life expectancy'))

        # plots about disease
        plots = []
        for col in COLUMNS[:-1]:
            plots.append(pn.pane.Plotly(
                px.line(selection, x='year', y=col, labels={col: 'Deaths per 100.000 people'}, color='country',
                        title=col.replace('[deaths]', ''))))

        gspec[0, :] = life_exp_plot
        gspec[1, 0] = plots[0]
        gspec[1, 1] = plots[1]
        gspec[2, 0] = plots[2]
        gspec[2, 1] = plots[3]
        gspec[3, 0] = plots[4]
        gspec[3, 1] = plots[5]

        return gspec

    def update(self, event):
        self.pane[1] = self.get_plot(self.checkbutton)

    def get_contents(self):
        return self.pane, self.button
