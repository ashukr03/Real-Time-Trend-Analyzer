import streamlit as st
from modules.scraper import get_headlines
from modules.processor import create_dataframe
from modules.visualizer import plot_sentiment_pie, plot_wordcloud, plot_category_sentiment
import matplotlib.pyplot as plt

st.set_page_config(page_title="Real-Time Trend Analyzer", layout="wide")
st.title("📰 Real-Time Trend Analyzer Dashboard")
st.write("Real-time sentiment & trend analysis using latest news headlines")
st.markdown("")

headlines = get_headlines()
if not headlines:
    st.warning("No headlines fetched. Check internet or RSS feed.")
else:
    df = create_dataframe(headlines)

    st.subheader("Latest Headlines")
    st.dataframe(df)
    st.markdown("")

# --- INFO CARDS (Beautiful UI Section) ---
st.markdown("""
<style>
.info-card {
    padding: 15px;
    border-radius: 12px;
    background-color: #f5f7fa;
    border-left: 6px solid #4a90e2;
    margin-bottom: 12px;
    font-size: 15px;
}
</style>

<div class='info-card'>
<b>🟢 Positive:</b> Growth, appreciation, success stories.<br>
<b>🟡 Neutral:</b> Factual or informational headlines.<br>
<b>🔴 Negative:</b> Conflicts, loss, issues, criticism.
</div>

<div class='info-card'>
<b>🧭 Category Sentiment:</b> Automatically detects headline topics like Politics, Business, Tech, Sports, Entertainment and shows emotional trend.
</div>

<div class='info-card'>
<b>📈 Sentiment Score (−1 to +1):</b><br>
• Score <b>&lt; 0</b> → headline is in negative tone.<br>
• Score <b>= 0</b> → neutral informational headline.<br>
• Score <b>&gt; 0</b> → positive / encouraging tone.<br><br>
The score shows the emotional intensity of the headline.
</div>

""", unsafe_allow_html=True)

# ------------------------------ MAIN LOGIC ------------------------------
st.markdown("")
headlines = get_headlines()
if not headlines:
    st.warning("No headlines fetched. Check internet or RSS feed.")
else:
    df = create_dataframe(headlines)  

    st.subheader("Sentiment Distribution(Pie Chart)")
    plot_sentiment_pie(df)
    st.markdown("") 


    st.subheader("Category-wise Sentiment Breakdown")
    plot_category_sentiment(df) 
    st.markdown("")                        

    st.subheader("Word Cloud of Headlines")
    st.markdown("") 
    plot_wordcloud(df)
    st.markdown("") 
    st.markdown("") 

    st.subheader("Sentiment Trend Over Headlines")
    fig, ax = plt.subplots()
    df['score'].plot(kind='line', ax=ax, color='blue', marker='o')
    ax.set_xlabel("Headline Index")
    ax.set_ylabel("Sentiment Score")
    ax.set_title("Sentiment Trend")
    st.pyplot(fig)
    st.markdown("") 


