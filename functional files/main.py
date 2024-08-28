import streamlit as st
from PIL import Image
import pickle


# Set title
st.title("Object Extraction, Identification and Analysis")

# Image upload section
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Image successfully uploaded!")

# User response section
user_response = st.text_area("Submit your response here:")

# Submit button
if st.button("Submit"):
    if uploaded_image is not None and user_response:
        st.success("Your response has been submitted!")
        st.write("**Your Response:**", user_response)
    else:
        st.error("Please upload an image and enter a response before submitting.")
