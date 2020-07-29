import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#fig = go.Figure()
app = dash.Dash(__name__)
server = app.server

# conn = sqlite3.connect("collegelist.db")
# df = pd.read_sql_query("select District from col_list limit 5;",conn)
# print(df)
#  District_df = df
District_df = pd.read_csv('col_list.csv')
reg =District_df['District']
#reg = reg.reset_index()
#reg.reset_index()
#reg =reg.head()
print(reg)



def create_dict_list_of_District():
    dictlist = []
    unique_list = District_df.District.unique()
    for District in unique_list:
        dictlist.append({'value': District, 'label': District})
    return dictlist
def dict_District_list(dict_list):
    District_list = []
    for dict in dict_list:
        District_list.append(dict.get('value'))
    return District_list
Dict_reg = create_dict_list_of_District()

#graph values for x & y calculated on basis of pandas command: df[df.['column name']==''corresonding value(in our case Region name).count()
app.layout = html.Div([
     html.Div([
         html.H1('Data Visualization Dashboard'),
         html.H2('Choose a Region name'),
         dcc.Dropdown(
             id='Regions-dropdown',
             options=Dict_reg,
             multi=False,
             value = 'Mumbai Suburban'
         ),
         # dcc.Graph(
         #     id='Regions_bar'
         #
         #  )
     ], style={'width': '40%', 'display': 'inline-block'}),
     html.Div([
        dcc.Graph(
        id='Regions-graph',
        figure={
            'data': [
                {'x': ['Mumbai Suburban','Mumbai City','Ratnagiri','Palghar','Sindhudurg','Raigad','Thane','Nashik','Chandrapur','Nagpur','Gondia','Bhandardara','Wardha','Ahmednagar','Pune','Kolhapur','Solapur','Satara','Sangli','Silvassa','Jalgaon','Nandurbar','Dhule','Gadchiroli'], 'y': [63, 41, 19, 18, 11, 57, 65, 112, 23, 132, 12, 16, 32, 93, 336, 71, 57, 55, 43, 1, 55,13,33,2], 'type': 'bar', 'name': 'Regions'}
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'No. of colleges per region',
                'xaxis': dict(
                    title= 'Regions',
                    titlefont=dict(
                    family='courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
                'yaxis' : dict(
                    title='No. of colleges',
                    titlefont=dict(
                    family='Helvetica, monospace',
                    size=18,
                    color='#7f7f7f'
                ))



            }
        }

     )

     ], style={'width': '100%', 'display': 'inline-block'}),
     html.Div([
         html.H2('Colleges Details for selected Region'),
         html.Table(id='my-table'),
         html.P(''),
     ], style={'width': '55%',  'display': 'inline-block'}),
])

@app.callback(Output('my-table', 'children'), [Input('Regions-dropdown', 'value')])
def generate_table(selected_dropdown_value, max_rows=15):
     District_df_filter = District_df[(District_df['District'].isin([selected_dropdown_value]))]
     District_df_filter = District_df_filter.sort_values(['District'], ascending=True)

     return [html.Tr([html.Th(col) for col in District_df_filter  .columns])] + [html.Tr([
         html.Td(District_df_filter.iloc[i][col]) for col in District_df_filter  .columns
     ]) for i in range(min(len(District_df_filter  ), max_rows))]



if __name__ == '__main__':
    app.run_server(debug=True)

