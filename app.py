import streamlit as st
import pandas as pd
from forecast_utils import forecast_stock, detect_sentiment
from advisor_agent import ask_investment_agent
from rag_helper import ask_policy_qa

st.set_page_config(page_title="FinForecast AI", layout="wide")
st.title("📉 FinForecast AI – Market Forecast & Investment Advisor")

uploaded = st.file_uploader("📤 Upload Stock Data (CSV)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
    st.subheader("📈 Forecasted Trend:")
    fig, message = forecast_stock(df)
    st.pyplot(fig)
    st.success(message)

st.divider()
st.header("🤖 Ask Investment Agent (Ollama)")
q1 = st.text_input("💬 e.g. Where should I invest in 2025?")
if q1:
    st.markdown(ask_investment_agent(q1))

st.divider()
st.header("📄 Ask Policy Guide (RAG - SEBI/RBI)")
q2 = st.text_input("💬 Ask about compliance or market regulation")
if q2:
    st.markdown(ask_policy_qa("docs/rbi_policy.pdf", q2))

st.divider()
st.header("📃 Upload Report (Sentiment Detection)")
txt = st.text_area("Paste financial report content here")
if txt:
    result = detect_sentiment(txt)
    st.info(f"🔍 Sentiment: **{result}**")
