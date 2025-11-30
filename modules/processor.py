import pandas as pd
from modules.sentiment_engine import analyze_sentiment

# --- CATEGORY DICTIONARY ----
categories = {
    "Politics": [
        "election", "government", "govt", "minister", "bjp", "congress", "rjd", "aap", "nda",
        "mahagathbandhan", "policy", "parliament", "rajya sabha", "lok sabha", "cm", "pm",
        "party", "vote", "poll", "political", "assembly", "campaign", "manifesto", "opposition",
        "cabinet", "coalition", "mp", "mla", "president", "governor", "judiciary", "supreme court",
        "sc", "high court", "verdict", "petition"
    ],

    "Business": [
        "stock", "market", "share", "nifty", "sensex", "economy", "economic", "trade", "finance",
        "business", "company", "ipo", "investment", "investor", "profit", "loss", "revenue",
        "earnings", "corporate", "industry", "inflation", "rbi", "bank", "monetary", "startup",
        "funding", "merger", "acquisition", "m&a", "fii", "dii", "gdp", "exports", "imports"
    ],

    "Sports": [
        "match", "tournament", "series", "player", "goal", "cricket", "football", "tennis",
        "badminton", "hockey", "fifa", "ipl", "world cup", "olympic", "medal", "run", "wicket",
        "innings", "coach", "team", "athlete", "score", "championship", "league"
    ],

    "Tech": [
        "technology", "tech", "ai", "artificial intelligence", "ml", "machine learning", 
        "software", "hardware", "app", "application", "data", "robot", "robotics", "gadget",
        "smartphone", "mobile", "laptop", "processor", "chip", "semiconductor",
        "cyber", "cybersecurity", "hacking", "hack", "cloud", "iot", "5g", "6g", "quantum",
        "digital", "electric vehicle", "ev", "isro", "nasa", "satellite", "space", "rocket"
    ],

    "Entertainment": [
        "movie", "film", "actor", "actress", "bollywood", "hollywood", "series", "web series",
        "trailer", "music", "song", "album", "celebrity", "star", "cinema", "director", "producer",
        "ott", "netflix", "amazon prime", "hotstar", "theatre", "release", "box office"
    ],

    "Health": [
        "health", "disease", "covid", "virus", "infection", "vaccine", "diabetes", "cancer",
        "heart", "mental health", "hospital", "doctor", "surgery", "medicine", "medical",
        "wellness", "fitness", "nutrition", "WHO", "clinical", "treatment", "deaths", "cases"
    ],

    "Science": [
        "scientist", "astronomy", "space", "galaxy", "research", "study", "experiment",
        "physics", "chemistry", "biology", "innovation", "discovery", "planet", "asteroid",
        "cosmos", "universe", "quantum", "laboratory"
    ],

    "Crime": [
        "murder", "killed", "crime", "attack", "blast", "terror", "terrorist", "fraud",
        "scam", "rape", "assault", "arrested", "illegal", "police", "investigation", "probe",
        "theft", "robbery", "violence", "misconduct", "charges", "court case"
    ],

    "World": [
        "usa", "china", "russia", "pakistan", "uk", "iran", "israel", "global", "international",
        "border", "conflict", "war", "strike", "un", "united nations", "world", "foreign",
        "treaty", "sanctions", "diplomacy", "embassy", "parley"
    ]
}


# --- CATEGORY DETECTION FUNCTION (FIXED) ---
def detect_category(text):
    text = text.lower()

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            return category

    return "Other"


# --- MAIN DATAFRAME CREATOR ---
def create_dataframe(headlines):
    df = pd.DataFrame({"headline": headlines})
    df["sentiment"], df["score"] = zip(*df["headline"].apply(analyze_sentiment))
    df["category"] = df["headline"].apply(detect_category)
    return df
