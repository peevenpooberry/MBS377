from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

app = Dash()
server = app.server

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data')

app.layout = [
    html.Div(children='Hello, Dash'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    )
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)