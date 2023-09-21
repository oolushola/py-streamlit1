import streamlit as st
import sender


st.set_page_config(layout="wide")
with st.container():
    st.header("Contact Me!")
    with st.form(key="contactme"):
        receiver = st.text_input(label="Email", label_visibility="hidden",
                                 placeholder="Enter your email")
        message = st.text_area(label="Message", placeholder="Drop a message")
        button = st.form_submit_button("SEND")
        if button:
            sender.sendEmail(message, receiver)
