# appp.py

import streamlit as st
import joblib

# Load the saved model
model = joblib.load('model.pkl')

st.title("🕵‍♂ Fake News Detection")

st.write("🔍 Enter the news content below to analyze if it's real or fake:")

news_text = st.text_area("📰 News Content")

if st.button("🔎 Analyze"):
    if news_text:
        prediction = model.predict([news_text])
        if prediction[0] == 1:
            st.success("✅ The news is REAL.")
        else:
            st.error("❌ The news is FAKE.")
    else:
        st.warning("⚠ Please enter the news content before analyzing.")
