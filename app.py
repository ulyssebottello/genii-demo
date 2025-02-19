import streamlit as st
import base64
import os
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Widget Demo Generator",
    layout="wide"
)

# Title
st.title("Widget Demo Generator")

# Default widget script
default_script = """<script 
    type="module" 
    project-id="1d2911e7-da17-4fc2-9705-0d45e91c7a9a"
    template="widget"
    src="https://genii-script.tolk.ai/lightchat.js"
    id="lightchat-bot">
</script>"""

# Function to get base64 from uploaded file
def get_image_base64_from_upload(uploaded_file):
    return base64.b64encode(uploaded_file.getvalue()).decode()

# Function to generate HTML content
def generate_html(image_base64, widget_script):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Widget Demo</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }}
        .background {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url(data:image/png;base64,{image_base64});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>
</head>
<body>
    <div class="background"></div>
    {widget_script}
</body>
</html>
"""

# Initialize widget script at the session state level
if 'widget_script' not in st.session_state:
    st.session_state.widget_script = default_script

# Main layout with equal width columns
col1, col2 = st.columns([1, 1])

# Left column: Image and buttons
with col1:
    st.subheader("Background Image")
    uploaded_file = st.file_uploader("Drop your background image here", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
        
        # Generate button and potential download
        if st.button("Generate Demo Page"):
            # Convert uploaded image to base64
            image_base64 = get_image_base64_from_upload(uploaded_file)
            
            # Generate HTML
            html_content = generate_html(image_base64, st.session_state.widget_script)
            
            # Provide download link
            st.download_button(
                label="Download HTML",
                data=html_content,
                file_name="demo.html",
                mime="text/html"
            )
            
            st.success("Demo page generated successfully!")

# Right column: Code editor
with col2:
    st.subheader("Widget Script")
    st.session_state.widget_script = st.text_area(
        "Edit script if needed:",
        st.session_state.widget_script,
        height=200
    ) 