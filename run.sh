#!/bin/bash

# This script installs the required Python packages and runs the Streamlit application.

echo "--- Installing dependencies from requirements.txt ---"
pip3 install -r requirements.txt

echo ""
echo "--- Starting Streamlit server ---"
# The OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES variable is a common fix for
# a "mutex lock" or "Abort trap: 6" crash on macOS when using libraries like TensorFlow.
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
python3 -m streamlit run app.py
