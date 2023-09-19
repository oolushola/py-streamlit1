import streamlit as st
from PIL import Image
import pandas


col1, col2 = st.columns(2)

with col1:
    st.image("assets/sola.jpg", width=300)

with col2:
    st.title("Olushola D. Odejobi")
    st.write("Github")
    bio = """
      I love building tools for enterprise, writing, speaking and punching my keyboard till something works. I graduated 2023 with a Masters degree in 2023, from Georgia Southern University with a focus on using python for remote sensing. I have worked with companies from various countries, such as the center for conservation georgraphy, to map and understand 
      """
    st.info(bio)

st.write("Below you can find some of the apps I have built. Feel free to contact me!")

leftcol, rightcol = st.columns(2)

content = pandas.read_csv("data.csv", sep=";")
print(content)
for index, data in content.iterrows():
    if index % 2 == 0:
        with leftcol:
            st.subheader(data["title"])
            st.write(data["description"])
            st.image("assets/images/" + data["image"])
            st.write("*[Source Code]*(https://www.google.com)")
    else:
        with rightcol:
            st.subheader(data["title"])
            st.write(data["description"])
            st.image("assets/images/" + data["image"])
