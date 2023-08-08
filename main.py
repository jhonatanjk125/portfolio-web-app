import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Jhonatan Gutiérrez")
    about = """Hello, I am Jhonatan! I am a Petroleum Engineer with experience in upstream operations in the Oil & Gas industry, specifically in drilling operations.
    I also have a passion for programming and learning languages! I've learned and developed some apps to hone my skills with python as you can see below."""
    st.info(about)