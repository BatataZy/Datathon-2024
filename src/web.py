from PIL.ImageFile import ImageFile
import streamlit as st
from yogi import read
from PIL import Image

st.write("Hello, guys, welcome to my first blog inspired in... (whatever!)")
st.latex(r"a + a r + a r^2 + a   r^3 + ar^4")
st.title("Títol") # Gran i en negreta
st.header("Header")
st.subheader("Subheader")
st.caption("This is the caption")
st.markdown("This is the markdown")
st.code("x = 2021")


# Pugem una imatge
image = Image.open("C:/Users/GABO.LOPEZ/Desktop/Gabo.png") # Path to image
st.image(image, caption = "Gabo posing") # C:/Users/GABO.LOPEZ/Desktop/Gabo.png
st.radio("Gender of this person?", ["Male", "Female"])
st.selectbox("Pick the ones you think are true (only at first glance)", ["Choose an option", "Stealer", "Honest", "None", "Both"])
st.caption("IS HE HOT??")
st.checkbox("Handsome")
st.checkbox("bold")
st.checkbox("Attractive")
st.button("Click if you would date him")
st.multiselect("What age do you thing he has?", ["<30", "between 30 and 50", ">50"])
st.select_slider("Would you say he is a person that would betray you?", [1, 2, 3, 4, 5])

# st.chat_input("Describe his look:")
