import panel as pn
import plotly.express as px


def heatmap(data, x, y, labels, text_auto=True):
    fig = px.imshow(
        data,
        x=x,
        y=y,
        labels=labels,
        text_auto=text_auto,
    )

    return pn.pane.Plotly(fig)
