import pandas as pd
import plotly.express as px

df = pd.read_csv('data/us-states.csv')

df['date'] = pd.to_datetime(df['date'])
df = df[(df['date'] >= '2020-03-01') & (df['date'] <= '2022-12-31')]

df['month_year'] = df['date'].dt.to_period('M').astype(str)
df_monthly = df.groupby(['month_year', 'state'], as_index=False)[['cases', 'deaths']].max()

df_monthly = df_monthly[(df_monthly['cases'] > 0) & (df_monthly['deaths'] > 0)]
df_monthly = df_monthly.sort_values(['month_year', 'state'])

fig = px.scatter(df_monthly,
                 x="cases",
                 y="deaths",
                 animation_frame="month_year",
                 animation_group="state",
                 size="cases",
                 color="state",
                 hover_name="state",
                 log_x=True,
                 log_y=True,
                 size_max=60,
                 range_x=[100, df_monthly['cases'].max() * 10],
                 range_y=[10, df_monthly['deaths'].max() * 10],
                 title="COVID-19 Dynamic Progression: Cases vs Deaths by US State",
                 labels={'cases': 'Total Cases (Log Scale)',
                         'deaths': 'Total Deaths (Log Scale)',
                         'month_year': 'Month',
                         'state': 'State'})

fig.update_layout(
    template='plotly_white',
    font_family="Arial",
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    legend_title_text='US State'
)

fig.write_html('animated_states.html')