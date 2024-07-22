import streamlit as st
from PIL import Image
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

img_file_buffer = st.camera_input("Camera access")
if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:ß
    # Should output: <class 'numpy.ndarray'>
    #st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
    
    
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    # To read image file buffer as a PIL Image:
    img = Image.open(uploaded_file)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:ß
    # Should output: <class 'numpy.ndarray'>
    #st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)