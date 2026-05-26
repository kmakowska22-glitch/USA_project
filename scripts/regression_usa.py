import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/compact.csv')

df_us = df[df['code'] == 'USA'].copy()
df_us['date'] = pd.to_datetime(df_us['date'])
df_us = df_us[(df_us['date'] >= '2019-01-01') & (df_us['date'] <= '2022-12-31')]
df_us = df_us.dropna(subset=['total_cases']).sort_values('date')

df_train = df_us.head(300).copy()
df_train['days_from_start'] = np.arange(len(df_train))

X = df_train[['days_from_start']]
y = df_train['total_cases']

model = LinearRegression()
model.fit(X, y)

future_days = np.arange(len(df_train) + 60).reshape(-1, 1)
predictions = model.predict(future_days)
start_date = df_train['date'].min()
future_dates = [start_date + pd.Timedelta(days=int(i)) for i in range(len(future_days))]

fig = go.Figure()

fig.add_trace(go.Scatter(x=df_train['date'], y=df_train['total_cases'],
                         mode='lines', name='Actual Cases',
                         line=dict(color='#00B4D8', width=4)))

fig.add_trace(go.Scatter(x=future_dates, y=predictions,
                         mode='lines', name='Linear Forecast',
                         line=dict(color='#E63946', dash='dash', width=2)))

fig.update_layout(
    template='plotly_white',
    font_family="Arial",
    title='Inferential Statistics: Projecting COVID-19 Case Trend (USA)',
    xaxis=dict(title='Date', showgrid=False, linecolor='gray', linewidth=1),
    yaxis=dict(title='Cumulative Cases', gridcolor='lightgray', linecolor='gray',
               linewidth=1, range=[0, max(predictions.max(), df_train['total_cases'].max()) * 1.1]),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.write_html('regression_usa.html')