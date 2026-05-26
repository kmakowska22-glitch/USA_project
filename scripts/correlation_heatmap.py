import pandas as pd
import plotly.express as px

df = pd.read_csv('data/compact.csv')

df_us = df[df['code'] == 'USA'].copy()
df_us['date'] = pd.to_datetime(df_us['date'])
df_us = df_us[(df_us['date'] >= '2021-01-01') & (df_us['date'] <= '2022-12-31')]

cols_to_correlate = [
    'new_cases_smoothed_per_million',
    'new_deaths_smoothed_per_million',
    'stringency_index',
    'reproduction_rate',
    'people_fully_vaccinated_per_hundred'
]

df_corr = df_us[cols_to_correlate].corr()

clean_labels = [
    'Daily Cases',
    'Daily Deaths',
    'Govt Restrictions',
    'Reproduction Rate',
    'Vaccination Rate'
]

fig = px.imshow(df_corr,
                x=clean_labels,
                y=clean_labels,
                color_continuous_scale='RdBu_r',
                zmin=-1, zmax=1,
                text_auto='.2f',
                aspect='auto',
                title='Pearson Correlation Matrix (USA 2021-2022)')

fig.update_layout(
    template='plotly_white',
    font_family="Arial",
    xaxis=dict(tickangle=45)
)

fig.write_html('correlation_heatmap.html')