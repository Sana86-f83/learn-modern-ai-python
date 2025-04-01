import streamlit as st
import random

# 🎯 List of motivational quotes
quotes = [
    "Believe in yourself and all that you are!",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else will do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay positive, work hard, make it happen!",
    "Difficulties in life are intended to make us better, not bitter.",
    "Don’t wait for opportunity. Create it.",
    "Success doesn’t just find you. You have to go out and get it."
]

# 🎨 Random background color generator
def get_random_color():
    colors = ["#FFB6C1", "#87CEFA", "#FFD700", "#90EE90", "#FFA07A", "#DDA0DD"]
    return random.choice(colors)

# 🌟 Streamlit UI
st.set_page_config(page_title="Motivation Booster", page_icon="💡")

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {get_random_color()};
        }}
        .quote-box {{
            background-color: black;
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            width: 80%;
            margin: auto;
            opacity: 60%;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        }}
        
        .stButton>button {{
            background-color: black !important;
            color: white !important;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold !important;
            padding: 10px 20px;
            border: white;
            cursor: pointer;
            margin-top:20px;
            margin-left:270px;
        }}
        .stButton>button:hover {{
            background-color: white !important;
            color:black !important;
            font-weight:bold !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌟 Daily Motivation Quotes 🌟")

# Show quote inside a styled box
random_quote = random.choice(quotes)
st.markdown(f'<div class="quote-box">💥{random_quote}💥</div>', unsafe_allow_html=True)

# Get New Quote Click button;
if st.button("Get New Quote"):
    st.rerun()

