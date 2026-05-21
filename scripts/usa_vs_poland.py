import pandas as pd
import plotly.express as px

print("reading data")
df = pd.read_csv('data/compact.csv')
print("Filtering")
df_comp = df[df['iso_code'].isin(['USA', 'POL'])].copy()
df_comp['date'] = pd.to_datetime(df_comp['date'])
print("Plot preparation")
fig = px.line(df_comp, 
              x='date', 
              y='new_cases_smoothed', 
              color='location',
              title='COVID-19: USA vs Polska (New infections smoothed-7-day average)',
              labels={'date': 'Data', 'new_cases_smoothed': 'New Cases', 'location': 'Country'})
fig.update_layout(template='plotly_dark', hovermode='x unified')
fig.write_html('usa_vs_poland.html')