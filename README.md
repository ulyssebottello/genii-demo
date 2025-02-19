# Widget Demo Generator

This Streamlit application allows you to generate demo pages that showcase a widget overlay on top of a background image. Perfect for creating personalized demos of chat widgets or similar overlay elements.

## Features

- Displays a background image preview
- Allows customization of the widget script
- Generates an HTML page with the widget overlaid on the background
- Provides options to download the HTML file or open it in a new tab

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. The background image (manon_capture.png) is automatically loaded and displayed
2. The widget script is pre-populated but can be modified if needed
3. Click "Generate Demo Page" to create the demo
4. Use the "Download HTML" button to save the file or click "Open Demo in New Tab" to view it directly

## Note

The generated HTML page will maintain the aspect ratio of the background image while ensuring it covers the entire viewport. The widget script will be properly injected and positioned over the background. 