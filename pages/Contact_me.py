import streamlit as st

st.header("Contact me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message:")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("I was pressed")