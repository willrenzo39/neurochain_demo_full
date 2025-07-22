import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

st.set_page_config(page_title="NeuroChain AI Supply Chain Demo", layout="wide")
st.title("🧠 NeuroChain: AI-Powered Demand Forecasting")

uploaded_file = st.file_uploader("Upload your historical sales CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Sample of uploaded data:")
    st.dataframe(df.head())

    df.columns = ["ds", "y"]
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    fig = px.line(forecast, x='ds', y='yhat', title='Forecasted Demand')
    st.plotly_chart(fig, use_container_width=True)