#!/bin/bash

# This script installs the required Python packages and runs the Streamlit application.

echo "--- Installing dependencies from requirements.txt ---"
pip3 install -r requirements.txt

echo ""
echo "--- Starting Streamlit server ---"
python3 -m streamlit run app.py
