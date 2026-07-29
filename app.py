import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Setting up the web page title
st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

# Creating a sidebar for user input
st.sidebar.header("Dashboard Controls")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, GOOG)", "AAPL")
time_period = st.sidebar.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

# Fetch the financial data
st.write(f"Fetching data for **{ticker_symbol.upper()}**...")
ticker_data = yf.Ticker(ticker_symbol)
df = ticker_data.history(period=time_period)

if not df.empty:
    # Build the interactive Plotly chart
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Market Data'
    ))
    
    fig.update_layout(
        title=f"{ticker_symbol.upper()} Live Share Price",
        yaxis_title="Stock Price (USD)",
        xaxis_title="Date",
        template="plotly_dark"
    )
    
    # Display the chart and the raw data table
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Recent Market Data")
    st.dataframe(df.tail())
else:
    st.error("No data found. Please check if the ticker symbol is correct.")
