import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="NSE MACD Dashboard", layout="wide")

st.title("📊 NSE MACD Dashboard")
st.write("Daily updated MACD, RSI, and ADX signals")

OUTPUT_DIR = "macd_output"

if not os.path.exists(OUTPUT_DIR):
    st.warning("⚠️ No output data found yet. Please wait for the first GitHub Action run (7 PM IST).")
else:
    bullish_file = os.path.join(OUTPUT_DIR, "bullish_stocks.csv")

    if os.path.exists(bullish_file):
        bullish_df = pd.read_csv(bullish_file)
        st.subheader("📈 Bullish Stocks Detected Today")
        st.dataframe(bullish_df)
    else:
        st.info("No bullish list found yet. It will appear after the daily run.")

    chart_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")]
    if chart_files:
        selected_chart = st.selectbox("Select a stock to view its chart", chart_files)
        chart_path = os.path.join(OUTPUT_DIR, selected_chart)
        st.image(chart_path, caption=selected_chart)
    else:
        st.info("No charts available yet.")
