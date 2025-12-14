# Sherlock Thorns: Plant Disease Detection AI

A web-based application built with Streamlit that uses a deep learning model to detect diseases in plant leaves. Users can upload an image of a plant leaf, and the AI will predict the disease and provide treatment advice.

## Features

- **Simple Web Interface**: Easy-to-use UI for uploading images.
- **Multi-Plant Support**: Detects diseases across a variety of plants, including:
  - Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, and Tomato.
- **Confidence Score**: Displays the model's confidence in its prediction.
- **Treatment Advice**: Offers actionable treatment suggestions for detected diseases.

## Prerequisites

- Python 3.x
- A pre-trained Keras model file named `plant_ai.keras` placed in the root directory.

## Setup & Installation

There are two ways to set up and run the application. The easiest method is using the provided shell script.

### Method 1: Using the `run.sh` Script (Recommended)

This script automates the installation of dependencies and starts the application server.

1.  **Navigate to the project directory:**
    ```bash
    cd /path/to/Sherlock-Thorns-Plant-Disease-Detection-AI
    ```

2.  **Make the script executable (only needs to be done once):**
    ```bash
    chmod +x run.sh
    ```

3.  **Run the script:**
    ```bash
    ./run.sh
    ```

### Method 2: Manual Installation

1.  **Navigate to the project directory.**

2.  **(Optional but Recommended) Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    python3 -m streamlit run app.py
    ```

## How to Use

1.  After starting the server using one of the methods above, open the local URL provided in your terminal (usually `http://localhost:8501`) in a web browser.
2.  Click the "Upload an image" button and select a JPG, PNG, or JPEG image of a plant leaf.
3.  The application will display the prediction, the model's confidence, and the uploaded image.
4.  Click the "Treatment Advice" button to get suggestions for how to handle the detected disease.