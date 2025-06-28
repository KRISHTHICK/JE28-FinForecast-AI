# JE28-FinForecast-AI
📉📈 FinForecast AI – Intelligent Market Advisor with RAG & AI Agents
🧠 Project Idea:
FinForecast AI is a smart AI-powered assistant for BFSI professionals and investors. It combines real-time financial insights, forecasting, and regulation-aware responses using:

🧠 AI Agents for interactive investment Q&A

📄 RAG to answer queries from financial policy documents (like SEBI, RBI PDFs)

📊 Forecast visualizations using historical stock data (CSV)

🔎 Sentiment-enhanced insights from uploaded reports

All running locally using Streamlit, Python, and Ollama

💡 Key Features:
Feature	Description
📤 Upload Stock CSV	Upload stock history (Open, Close, Volume) for analysis
📈 AI Forecast & Trend Agent	Predict trends using basic modeling and explain them via AI agent
🧠 AI Investment Advisor Agent	Ask an AI questions like “Where to invest in 2025?” using Ollama
📄 RAG from SEBI/RBI PDFs	Ask regulatory queries from financial compliance docs
💬 Sentiment Detection (Bonus)	Upload report text to detect if tone is bullish, bearish, or neutral


# 📉 FinForecast AI – Intelligent Investment and Compliance Assistant

A complete GenAI-powered app that:
- Forecasts market trends from stock CSVs
- Uses an Ollama-powered local investment AI agent
- Performs RAG-based QA over SEBI/RBI PDFs
- Detects sentiment from reports

## 🚀 How to Run

```bash
git clone https://github.com/yourname/FinForecast-AI.git
cd FinForecast-AI
pip install -r requirements.txt
ollama serve
ollama run tinyllama
streamlit run app.py
