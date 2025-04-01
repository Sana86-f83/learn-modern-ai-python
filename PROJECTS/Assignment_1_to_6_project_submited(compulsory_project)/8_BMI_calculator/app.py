import streamlit as st

st.markdown("""
    <style>
        .stApp{{
            background-color: black !important;
            color: white !important;

        }}
        .stMarkdown, .stTitle, .stTextInput, .stNumberInput {            
            color: green !important;
            margin-top:20px;
            
        }
    </style>
    """, unsafe_allow_html=True
)
# page_title
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="background-color: green; color: white; padding: 8px; border-radius: 10px;">
            📊 BMI Calculator
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# User Input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.1f")
height = st.number_input("Enter your height (meters):", min_value=0.5, format="%.2f")

# Enter Button
if st.button("Calculate BMI"):
    # BMI Calculation Function
    def calculate_bmi(weight, height):
        if height == 0:
            return None
        return round(weight / (height ** 2), 2)

    if weight and height:
        bmi = calculate_bmi(weight, height)
        if bmi:
            st.markdown(f"""<p style="color:yellow;font-size:24px;font-weight:bold;">📊 Your BMI: **{bmi}**</p>""",unsafe_allow_html=True)

            # BMI Category
            if bmi < 18.5:
                st.warning("⚠️ Underweight")
            elif 18.5 <= bmi < 24.9:
                st.success("✅ Normal Weight")
            elif 25 <= bmi < 29.9:
                st.info("⚠️ Overweight")
            else:
                st.error("❌ Obese")

# Footer
st.markdown("""
    <hr>
    <p style="text-align:center; color:green;font-size:18px;">Developed by <span style="color:yellow;">Sana Faisal</span> | © 2024 All Rights Reserved</p>
    """, unsafe_allow_html=True
)
