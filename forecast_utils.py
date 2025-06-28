import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from textblob import TextBlob

def forecast_stock(df):
    df = df.dropna()
    df['Index'] = range(len(df))
    model = LinearRegression()
    X = df[['Index']]
    y = df['Close']
    model.fit(X, y)
    future = model.predict(np.array([[len(df) + i] for i in range(5)]))

    fig, ax = plt.subplots()
    ax.plot(df['Index'], df['Close'], label="Historical")
    ax.plot(range(len(df), len(df)+5), future, label="Forecast", linestyle='--')
    ax.set_title("Stock Forecast")
    ax.legend()
    return fig, "Forecast shows future trend based on linear regression."

def detect_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0.2:
        return "Bullish"
    elif blob.sentiment.polarity < -0.2:
        return "Bearish"
    else:
        return "Neutral"
