import streamlit as st
from modules.scraper import get_headlines
from modules.processor import create_dataframe
import pandas as pd


st.title("🧐 Sentiment Analysis")
st.write("Detailed sentiment analysis of latest news headlines")

headlines = get_headlines()
if not headlines:
    st.warning("No headlines fetched. Check internet or RSS feed.")
else:
    df = create_dataframe(headlines)
    
    # Filter options
    sentiment_filter = st.multiselect(
        "Filter by Sentiment",
        options=df['sentiment'].unique(),
        default=df['sentiment'].unique()
    )
    filtered_df = df[df['sentiment'].isin(sentiment_filter)]
    
    st.subheader("Filtered Headlines")
    st.dataframe(filtered_df.reset_index(drop=True))
    
    # Top positive & negative
    st.subheader("Top Positive Headlines")
    st.dataframe(filtered_df.sort_values(by="score", ascending=False).head(5).reset_index(drop=True))
    
    st.subheader("Top Negative Headlines")
    st.dataframe(filtered_df.sort_values(by="score", ascending=True).head(5).reset_index(drop=True))
