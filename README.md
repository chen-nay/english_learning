# Vocabulary Learn Project

This is a simple web application designed to help you learn vocabulary. It consists of an `index.html` frontend and a Python backend that manages word statuses in JSON files.

## Features

- **Vocabulary Browsing**: View words, phonetic symbols, definitions, synonyms, and example sentences.
- **Track Progress**: Mark words as "known" (认识) or "unknown" (不认识). Statuses are saved directly to JSON files on the server.
- **Dynamic Wordbooks**: Automatically loads any `.json` vocabulary files placed in the `wordbook/` directory.
- **Focus Mode**: Toggle between detailed view and a "Focus Mode" (eye icon) that hides details to test your memory. Individual cards can be revealed by clicking their specific eye icon.

## How to Run

To run this project, you need to start the Python backend server and then open the `index.html` file in your web browser.

### 1. Start the Python Backend Server

Navigate to the project's root directory in your terminal and run the Python server:

```bash
python3 server.py
```

This will start a local HTTP server on port **9001**. You should see a message like:
`serving at port 9001`

Keep this terminal window open as long as you are using the application.

### 2. Open the Frontend

After starting the backend server, open your web browser and navigate to the `index.html` file using the following URL:

http://localhost:9001

### 3. Usage

-   **Select a Wordbook**: Choose a vocabulary list from the sidebar. (To add new books, simply drop a `.json` file into the `wordbook/` folder).
-   **Review Words**:
    -   Click **认识 (Known)** or **不认识 (Unknown)** to update your progress.
    -   Click the **Eye Icon** (👁️) in the top right to toggle "Focus Mode".
    -   In Focus Mode, click the small eye icon on a card to peek at its details.
-   **Audio**: Click the speaker icon to hear the pronunciation.

Enjoy learning!