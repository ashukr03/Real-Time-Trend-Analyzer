import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import pandas as pd


def plot_sentiment_pie(df):
    counts = df['sentiment'].value_counts()
    fig, ax = plt.subplots(figsize=(2.5, 2.5))   # 🔥 Smaller pie chart
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%",
           colors=['green','red','grey'])
    st.pyplot(fig)

def plot_wordcloud(df):
    text = " ".join(df['headline'].tolist())
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.image(wc.to_array(), use_container_width=True)  # 🔥 Fixed deprecation warning

def plot_category_sentiment(df):
    grouped = df.groupby(["category", "sentiment"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(7, 4))
    grouped.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")
    st.pyplot(fig)

