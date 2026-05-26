import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data/compact.csv')

df_us = df[df['code'] == 'USA'].copy()
df_us['date'] = pd.to_datetime(df_us['date'])
df_us = df_us[(df_us['date'] >= '2020-12-01') & (df_us['date'] <= '2022-12-31')]

cols = ['people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred']
df_us[cols] = df_us[cols].ffill().fillna(0)
df_us = df_us.sort_values('date')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_us['date'], y=df_us['people_vaccinated_per_hundred'],
    mode='lines',
    line=dict(width=1, color='#A7F3D0'),
    fill='tozeroy',
    name='At Least One Dose'
))

fig.add_trace(go.Scatter(
    x=df_us['date'], y=df_us['people_fully_vaccinated_per_hundred'],
    mode='lines',
    line=dict(width=1, color='#34D399'),
    fill='tozeroy',
    name='Fully Vaccinated'
))

fig.add_trace(go.Scatter(
    x=df_us['date'], y=df_us['total_boosters_per_hundred'],
    mode='lines',
    line=dict(width=1, color='#059669'),
    fill='tozeroy',
    name='Booster Dose'
))

fig.update_layout(
    title='COVID-19 Vaccination Progress in USA (Per 100 People)',
    template='plotly_white',
    font_family="Arial",
    xaxis=dict(title='Date', showgrid=False, linecolor='gray', linewidth=1),
    yaxis=dict(title='Percent of Population (%)', showgrid=True, gridcolor='lightgray', range=[0, 100]),
    hovermode='x unified',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.write_html('vaccinations_usa.html')