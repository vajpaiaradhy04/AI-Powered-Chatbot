# -AI-Powered-Chatbot
This project is a web-based AI-powered chatbot built using Python, FastAPI, NLTK, and SQLite, designed to deliver intelligent, context-aware responses for customer support or FAQ automation. It features a real-time frontend interface and stores all user-bot interactions in a local database for future analysis.

## Running and Debugging

To run and debug the FastAPI backend server locally, follow these steps:

1. Ensure you have Python installed (version 3.7 or higher recommended).
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Start the FastAPI server with hot reload enabled by running:
   ```
   uvicorn main:app --reload
   ```
4. Open your browser and navigate to `http://localhost:8000` to access the chatbot frontend.
5. Any changes to the backend code will automatically reload the server for easier debugging.

Alternatively, you can run the provided script `run_server.bat` to start the server easily on Windows. Note: In PowerShell, run the script with `.\run_server.bat` to execute it from the current directory.

