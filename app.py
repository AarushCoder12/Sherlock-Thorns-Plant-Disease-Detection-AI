import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

# Cache the model loading to prevent reloading on every interaction
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("PlantAImodel(94% train to 81% valid).keras")
    return model

# Load the pre-trained model using the cached function
model = load_model()

#Website title and description
st.title("Sherlock Thorns: Plant Disease Detection AI")
st.write("Upload an image of a plant leaf to detect diseases. The plant must be one of the following: Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato.")


##File uploader
#uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

#if uploaded_file is not None:
#    # Open image
#    image = Image.open(uploaded_file).convert("RGB")
#    img = np.array(image)

 #    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

 #   # Define green color range (leaf)
 #   lower_green = np.array([15, 20, 20])
 #   upper_green = np.array([100, 255, 255])

#    # Create mask for leaf
#    mask = cv2.inRange(hsv, lower_green, upper_green)

#    # Create black background
#    black_bg = np.zeros_like(img)

#    # Keep only leaf pixels
#    segmented = cv2.bitwise_and(img, img, mask=mask)

#    # Resize & normalize
#   target_size = (224, 224)
#    img_array = cv2.resize(segmented, target_size) / 255.0
 #   img_array = np.expand_dims(img_array, axis=0)

    # Predict
 #   predictions = model.predict(img_array)
#    index = np.argmax(predictions)
 #   confidence = predictions[0][index] * 100


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
    confidence = predictions[0][index]*100

    #Class names
    class_names = [
    "Apple_AppleScab",
    "Apple_BlackRot",
    "Apple_AppleRust",
    "Apple_Healthy",
    "Blueberry_Healthy",
    "Cherry_PowderyMildew",
    "Cherry_Healthy",  
    "Corn_CercosporaLeaTfSpot",
    "Corn_CommonRust",
    "Corn_NorthernLeafBlight",
    "Corn_Healthy",
    "Grape_BlackRot",
    "Grape_Esca",
    "Grape_LeafBlight",
    "Grape_Healthy",
    "Orange_Haunglongbing",  
    "Peach_BacterialSpot",
    "Peach_Healthy",
    "Pepper_BacterialSpot",
    "Pepper_Healthy",#
    "Potato_EarlyBlight",
    "Potato_LateBlight",
    "Potato_Healthy",
    "Raspberry_Healthy",
    "Soybean_Healthy",
    "Squash_PowderyMildew",
    "Strawberry_LeafScorch",
    "Strawberry_Healthy",
    "Tomato_BacterialSpot",
    "Tomato_EarlyBlight",
    "Tomato_LateBlight",
    "Tomato_LeafMold",
    "Tomato_SeptoriaLeafSpot",
    "Tomato_SpiderMites",
    "Tomato_TargetSpot",
    "Tomato_YellowLeafCurlVirus",
    "Tomato_MosaicVirus",   
    "Tomato_Healthy",
]

 
    if class_names[index].endswith("Healthy"):
        plant_name = class_names[index].split("_")[0]
        st.success(plant_name+f" plant is healthy: No disease detected.")
    else: 
        plant_name = class_names[index].split("_")[0]
        st.write(f"The detected disease for {plant_name} is {class_names[index].split('_')[1]}")
    st.write(f"I am {confidence:.1f}% Confident my Response is Accurate")
    st.image(image,caption="Uploaded Image", use_column_width=True)
     
    if st.button("Treatment Advice"):
        if class_names[index].endswith("Healthy"):
            st.info("No treatment needed. Your plant is healthy!")
        elif class_names[index].endswith("AppleScab"):
            st.warning("Apply fungicides containing captan or myclobutanil. Remove and destroy infected leaves.")
        elif class_names[index].endswith("Rust"):
            st.warning("Use fungicides containing sulfur or copper-based products. Remove and destroy infected leaves.")
        elif class_names[index].endswith("PowderyMildew"):
            st.warning("Apply fungicides containing neem oil or potassium bicarbonate. Increase air circulation around plants.")
        elif class_names[index].endswith("LeafScorch"):
            st.warning("Ensure proper watering and avoid overhead irrigation. Apply mulch to retain soil moisture.")
        elif class_names[index].endswith("BacterialSpot"):
            st.warning("Use copper-based bactericides. Remove and destroy infected plant parts.")
        elif class_names[index].endswith("Rot"):
            st.warning("Apply fungicides containing captan or myclobutanil. Remove and destroy infected leaves.")
        elif class_names[index].endswith("Blight"):
            st.warning("Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected leaves.")
        elif class_names[index].endswith("Esca"):
            st.warning("Prune and remove infected wood. Apply fungicides containing copper-based products.")
        elif class_names[index].endswith("GrayLeafSpot"):
            st.warning("Apply fungicides containing azoxystrobin or pyraclostrobin. Remove and destroy infected leaves.")
        elif class_names[index].endswith("MosaicVirus"):
            st.warning("Remove and destroy infected plants. Use disease-free planting material.")
        elif class_names[index].endswith("SpiderMites"):
            st.warning("Use insecticidal soap or neem oil. Increase humidity and water plants regularly.")
        elif class_names[index].endswith("Septorialeafspot"):
            st.warning("Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected leaves.")
        elif class_names[index].endswith("TargetSpot"):
            st.warning("Apply fungicides containing azoxystrobin or pyraclostrobin. Remove and destroy infected leaves.")
        elif class_names[index].endswith("YellowLeafCurlVirus"):
            st.warning("Use insecticidal soap or neem oil. Increase humidity and water plants regularly.")
        elif class_names[index].endswith("Leaf_Mold"):
            st.warning("Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected leaves.")
        elif class_names[index].endswith("Haunglongbing"):
            st.warning("Use insecticidal soap or neem oil. Increase humidity and water plants regularly.")
        elif class_names[index].endswith("CercosporaLeafSpot"): 
            st.warning("Apply fungicides containing azoxystrobin or pyraclostrobin. Remove and destroy infected leaves.")
