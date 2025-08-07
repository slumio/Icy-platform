#!/bin/bash

# This script starts both the backend and frontend servers for development.

# --- Step 1: Start the Backend Server ---
echo "--- Starting Backend Server (FastAPI) on http://localhost:8000 ---"

# Navigate to the backend directory to run the server command
cd backend/

# Run the uvicorn server as a background process using '&'
# The --reload flag automatically restarts the server when you change the code.
uvicorn src.main:app --reload &

# Capture the Process ID (PID) of the backend server
BACKEND_PID=$!

# Navigate back to the root directory
cd ..

# --- Step 2: Start the Frontend Server ---
echo "--- Starting Frontend Server (React) on http://localhost:3000 ---"

# Navigate to the frontend directory
cd frontend/

# Run the React development server in the foreground
npm start

# --- Step 3: Cleanup ---
# When you stop the frontend (e.g., with Ctrl+C), this line will automatically
# stop the backend server process that was running in the background.
kill $BACKEND_PID