import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

# Cache the model loading to prevent reloading on every interaction
@st.cache_resource
def load_model():
    model = keras.models.load_model("plant_ai.keras")
    return model

# Load the pre-trained model using the cached function
model = load_model()

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
             "Corn_CercosporaLeafSpot",
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
             "Pepper_Healthy",
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
             "Tomato_Leaf_Mold",
             "Tomato_Septoria_leaf_spot",
             "Tomato_SpiderMites",
             "Tomato_TargetSpot",
             "Tomato_YellowLeafCurlVirus",
             "Tomato__MosaicVirus",
             "Tomato_Healthy",
             
    ]
    st.subheader("Prediction")
    if class_names[index].endswith("Healthy"):
        plant_name=class_names[index].split("_")[0]
        st.success(plant_name+f" plant is healthy: No disease detected.")
    else: 
        st.write(f"The detected disease is: {class_names[index]}")
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
        elif class_names[index].endswith("Septoria_leaf_spot"):
            st.warning("Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected leaves.")
        elif class_names[index].endswith("TargetSpot"):
            st.warning("Apply fungicides containing azoxystrobin or pyraclostrobin. Remove and destroy infected leaves.")
        elif class_names[index].endswith("YellowLeafCurlVirus"):
            st.warning("Use insecticidal soap or neem oil. Increase humidity and water plants regularly.")
        elif class_names[index].endswith("Leaf_Mold"):
            st.warning("Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected leaves.")
        elif class_names[index].endswith("Haunglongbing"):
            st.warning("Use insecticidal soap or neem oil. Increase humidity and water plants regularly.")
        else: 
            st.warning("The disease is not recognized. Consult a plant expert for further advice.")
