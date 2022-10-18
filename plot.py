import plotly.express as pl
import json
import plotly
import pandas as pd

class Plot():
    
    def plot(self, data):
        fig = pl.line(data, x=data.iloc[:, 0], y=data.iloc[:, 4])
        fig.update_layout(title_text= 'YEARLY REPORT')
        fig.update_xaxes(title_text = 'Time')
        fig.update_yaxes(title_text = 'Stock Price')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON