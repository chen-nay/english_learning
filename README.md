# Vocabulary Learn Project

This is a simple web application designed to help you learn vocabulary. It consists of an `index.html` frontend and a Python backend that manages word statuses in JSON files.

## Features

- Display words and their definitions.
- Mark words as "known" or "unknown".
- Persist word statuses in JSON files on the server-side.

## How to Run

To run this project, you need to start the Python backend server and then open the `index.html` file in your web browser.

### 1. Start the Python Backend Server

Navigate to the project's root directory in your terminal and run the Python server:

```bash
python3 server.py
```

This will start a local HTTP server on port 8000 (or the port specified in `server.py`). You should see a message like "serving at port 8000". Keep this terminal window open as long as you are using the application.

### 2. Open the Frontend

After starting the backend server, open your web browser and navigate to the `index.html` file.

You can usually do this by typing `http://localhost:8000/index.html` in your browser's address bar, assuming the server is running on port 8000 and `index.html` is in the root directory.

### 3. Usage

-   Select a vocabulary list from the sidebar.
-   Browse through the words.
-   Click "认识" (known) or "不认识" (unknown) to update the status of each word. The status will be saved to the corresponding JSON file.

Enjoy learning!
