import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the pre-trained model
model=tf.keras.models.load_model("plant_ai.keras")

#Website title and description
st.title("Sherlock Thorns: Plant Disease Detection AI")
st.write("Upload an image of a plant leaf to detect diseases. The plant must be one of the following: Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, Tomato.")

#File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    #Open image
    image = Image.open(uploaded_file)

    #Resize and preprocess the image    
    target_size = (224, 224)
    img_array = np.array(image.resize(target_size)) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    #Predict the class
    predictions = model.predict(img_array)
    index = np.argmax(predictions)
    confidence = 

    #Class names
    class_names = [
             "Apple_AppleScab",
             "Apple_BlackRot",
             "Apple_Cedar_AppleRust",
             "Apple_Healthy",
             "Cherry_Healthy",
             "Cherry_PowderyMildew",
             "Corn_CommonRust",
             "Corn_GrayLeafSpot",
             "Corn_Healthy",
             "Corn_NorthernLeafBlight",
             "Grape_BlackRot",
             "Grape_Esca",
             "Grape_Healthy",
             "Grape_LeafBlight",
             "Peach_BacterialSpot",
             "Peach_Healthy",
             "Pepper_BacterialSpot",
             "Pepper_Healthy",
             "Potato_EarlyBlight",
             "Potato_Healthy",
             "Potato_LateBlight",
             "Strawberry_Healthy",
             "Strawberry_LeafScorch",
             "Tomato_BacterialSpot",
             "Tomato_EarlyBlight",
             "Tomato_Healthy",
             "Tomato_LateBlight",
    ]
    st.subheader("Prediction")
    if class_names[index].endswith("Healthy"):
        plant_name=class_names[index].split("_")[0]
        st.success(plant_name+f" plant is healthy: No disease detected.")
    else: 
        st.write(f"The detected disease is: {class_names[index]}")
    st.image(image,caption="Uploaded Image", use_column_width=True)

    

