import streamlit as st

with st.container():
    st.header("Contact Me!")
    st.text_input(label="Email", label_visibility="hidden",
                  placeholder="Enter your email")
    st.text_area(label="Message", placeholder="Drop a message")
    st.button("Leave a Message!", type="secondary")
