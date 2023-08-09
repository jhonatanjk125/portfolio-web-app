import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Jhonatan Gutiérrez")
    about = """Hello, I am Jhonatan! I am a Petroleum Engineer with experience in upstream operations in the Oil & Gas industry, specifically in drilling operations.
    I also have a passion for programming and learning languages! I've learned and developed some apps to hone my skills with python as you can see below."""
    st.info(about)

content1 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in dataframe[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")