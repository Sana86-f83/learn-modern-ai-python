import pyttsx3
import streamlit as st
import random
import threading  # Multithreading library


# 🎯 List of motivational quotes
quotes = [
    "Believe in yourself and all that you are!<br>🔹 خود پر اور اپنی صلاحیتوں پر یقین رکھیں!",
    "Your limitation—it’s only your imagination.<br>🔹 آپ کی حدیں صرف آپ کے تصور میں ہیں۔",
    "Push yourself, because no one else will do it for you.<br>🔹 خود کو آگے بڑھائیں، کیونکہ کوئی اور یہ آپ کے لیے نہیں کرے گا۔",
    "Great things never come from comfort zones.<br>🔹 عظیم کامیابیاں کبھی بھی آرام دہ علاقوں سے حاصل نہیں ہوتیں۔",
    "Dream it. Wish it. Do it.<br>🔹 خواب دیکھیں، خواہش کریں، اور اسے حقیقت بنائیں۔",
    "Stay positive, work hard, make it happen!<br>🔹 مثبت رہیں، محنت کریں، اور اسے ممکن بنائیں!",
    "Difficulties in life are intended to make us better, not bitter.<br>🔹 زندگی کی مشکلات ہمیں مضبوط بنانے کے لیے آتی ہیں، نہ کہ ہمیں مایوس کرنے کے لیے۔",
    "Don’t wait for opportunity. Create it.<br>🔹 موقع کا انتظار نہ کریں، اسے خود تخلیق کریں۔",
    "Success doesn’t just find you. You have to go out and get it.<br>🔹 کامیابی خود چل کر آپ کے پاس نہیں آتی، آپ کو اسے حاصل کرنا پڑتا ہے۔"
]

def get_random_color():#9c2d0e
    colors = ["#02dbbb", "#87CEFA", "#0fab87", "#90EE90", "#FFA07A", "#e3af5b","#b4cc66","#178518","#e65364"]
    return random.choice(colors)

st.set_page_config(page_title="Motivation Booster",page_icon="💡",layout="centered")

st.markdown(f"""
    <style>
        .stApp{{
            background-color:{get_random_color()}
        }}
        .quote-box{{
        background-color:black;
        padding:20px;
        color:white;
        width:100%;
        text-align:center;
        font-size:24px;
        font-weight:bold;
        margin:auto;
        opacity:60%;
        border-radius:10px;
        text-align:center:
        border:4px solid white;
        box-shadow:15px 15px 15px rgba(20,20,0,0.8);
    }} 

    .stButton>button{{
        margin-top:20px;
        padding:10px;
        font-size:20px;
        width:20%;
        margin-left:270px;
        background-color:black !important:
        color:white;
        border-radius:50px;
        border:4px solid white;
    }}    
   .stButton>button:hover {{
            background-color: white !important;
            color:black !important;
            font-weight:bold !important;
            border:4px solid black;
    }}                    
    </style>
    """,
unsafe_allow_html=True
)

st.title("🌟 Daily Motivation Quotes 🌟")

# Random Quote Selection
if "random_quote" not in st.session_state:
    st.session_state.random_quote = random.choice(quotes)

# 🗣️ Text-to-Speech Function (Runs in a separate thread)
def speak_quote(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)  # Speech Speed
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()  # Run TTS in background


# Show Quote
st.markdown(f'<div class=quote-box>💥 {st.session_state.random_quote} 💥</div>', unsafe_allow_html=True)

# 🎤 Speak Quote Button
if st.button("🔊 Speak Quote"):
    speak_quote(st.session_state.random_quote.split("<br>")[0])  

# 🔄 New Quote Button
if st.button("Get New Quote"):
    st.session_state.random_quote = random.choice(quotes)
    st.rerun()


