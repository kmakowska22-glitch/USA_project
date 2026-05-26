import pandas as pd
import plotly.express as px

df = pd.read_csv('data/compact.csv')

df_comp = df[df['code'].isin(['USA', 'POL'])].copy()
df_comp['date'] = pd.to_datetime(df_comp['date'])
df_comp = df_comp[(df_comp['date'] >= '2019-01-01') & (df_comp['date'] <= '2022-12-31')]
df_comp = df_comp.dropna(subset=['new_cases_smoothed'])

fig = px.line(df_comp,
              x='date',
              y='new_cases_smoothed',
              color='country',
              title='COVID-19: Weekly Smoothed New Infections (USA vs Poland)',
              labels={'date': 'Date', 'new_cases_smoothed': 'New Cases', 'country': 'Country'})

fig.update_layout(
    template='plotly_white',
    font_family="Arial",
    title_font_size=20,
    xaxis=dict(showgrid=False, linecolor='gray', linewidth=1, tickangle=45),
    yaxis=dict(gridcolor='lightgray', linewidth=1),
    hovermode='x unified',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.write_html('usa_vs_poland.html')