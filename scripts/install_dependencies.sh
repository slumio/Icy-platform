#!/bin/bash

# This script installs all necessary dependencies for both the
# Python backend and the Node.js frontend.

echo "--- Installing Backend Dependencies (Python) ---"
pip install -r backend/requirements.txt

echo "" # Add a newline for better readability
echo "--- Installing Frontend Dependencies (Node.js) ---"
cd frontend
npm install
cd ..

echo ""
echo "--- ✅ Installation Complete ---"