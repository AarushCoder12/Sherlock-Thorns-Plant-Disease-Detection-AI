import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import streamlit.components.v1 as components

# Cache the model loading to prevent reloading on every interaction
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("PlantAImodel_final_Jan_11_4PM.keras")
    return model

# Load the pre-trained model using the cached function
model = load_model()
#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Choose the app mode",
                                ["Home", "About App and Creators", "Plant Disease Detection AI"])
if app_mode == "Home":
# Home Page Content
    html_content = """
<style>
    #heading {
        text-align: center;
        font-size: 2.5em;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    #paragraph {
        text-align: center;
        font-size: 1.1em;
        color: rgb(8, 188, 149);
        font-family: monospace;
        white-space: pre-wrap;
        margin: 20px 0;
    }
    .header-container {
        text-align: center;
        padding: 20px;
    }
    .instructions {
        text-align: center;
        font-size: 1.1em;
        font-family: monospace;
        line-height: 1.6;
        margin: 20px 0;
    }
    .instructions ul {
        text-align: left;
        display: inline-block;
    }
    #list{
    font-family:monospace;
    text-align:center;
    }
   
</style>
<div class="header-container">
    <h1 id="heading">Sherlock Thorns</h1>
    <h2 id="heading">A Plant Disease Detection AI</h2>
    <pre id="paragraph">The plants that our AI supports are: 
Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato
    </pre>
</div>

<div class="instructions">
    <h3>How to Use Our AI:</h3>
    <ul>
        <li id="list">The two arrows in the top-left corner open the sidebar for easy navigation</li>
        <li id="list">In the "About App and Creators" page, learn about the educators who created this AI</li>
        <li id="list">In the "Plant Disease Detection AI" page, click "Browse files" to upload an image</li>
        <li id="list">After uploading, the AI will detect the disease and show treatment advice</li>
    </ul>
</div>
"""

    st.markdown(html_content, unsafe_allow_html=True)

    # Try to display background image if it exists
    try:
        background_image = Image.open("SherlockThornsBackround.png")
        st.image(background_image, use_column_width=True)
    except FileNotFoundError:
        pass
elif app_mode == "About App and Creators":
    more_html_content= """
    <style>
        #Heading {
            text-align: center;
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        #AboutUs {
            text-align: center;
            font-size: 1.1em;
            color: #34495e;
            font-family: monospace;
            white-space: pre-wrap;
        }
    </style>
    <h1 id="Heading">About App and Creators</h1>
    <body background-color:#07aa6e>
    <pre id="AboutUs">This is Sherlock Thorns, our plant disease detective AI. We created this website to help farmers, ranchers, gardeners, and everyday people 
    easily identify diseases affecting their plants. Our inspiration came from real-life experiences, including our parents, who wanted to start a garden but struggled 
    to identify diseases affecting their plants. We also noticed that even experienced farmers can have difficulty detecting plant diseases across large areas of land. 
    These challenges motivated us to develop Sherlock Thorns, an AI-powered tool designed to make plant disease detection faster, more accurate, and more accessible for 
    everyone.
    </pre>
    </body>
"""
    st.markdown(more_html_content, unsafe_allow_html=True)

elif app_mode == "Plant Disease Detection AI":
    even_more_html_content= """
    <style>
    #AI{
    text-align:center;
    font-size:150px;
    color:2c3e50;
    margin-bottom 10px;
    }
    </style>

    <body>
    <h1 id="AI"> Mr. Thorns: Our AI </h1>
    </body>
    """
    st.markdown(even_more_html_content, unsafe_allow_html=True)

    #Website title and description
    st.markdown("---")
    st.write("Upload an image of a plant leaf to detect diseases.")

    #File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

    # Class names
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
        "Tomato_LeafMold",
        "Tomato_SeptoriaLeafSpot",
        "Tomato_SpiderMites",
        "Tomato_TargetSpot",
        "Tomato_YellowLeafCurlVirus",
        "Tomato_MosaicVirus",   
        "Tomato_Healthy",
    ]

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess
        target_size = (224, 224)
        img_array = np.array(image.resize(target_size)) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)
        index = np.argmax(predictions)
        confidence = predictions[0][index] * 100

        # Output
        if class_names[index].endswith("Healthy"):
            plant_name = class_names[index].split("_")[0]
            st.success(f"{plant_name} plant is healthy: No disease detected.")
        else:
            plant_name = class_names[index].split("_")[0]
            disease = class_names[index].split("_")[1]
            st.error(f"The detected disease for {plant_name} is {disease}")

        st.write(f"I am {confidence:.1f}% confident my response is accurate.")

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
    else:
        st.warning("Please upload an image to continue.")
