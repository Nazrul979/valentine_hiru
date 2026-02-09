import streamlit as st


val = "Will you be my Valentine!!?❤️❤️"


#Header + larger text size + center alignment
st.markdown(
    """
    <style>
    .big-font {
        font-size: 4rem !important;
        font-weight: bold;
        text-align: center;
        color: #7b1113;
        font-family: 'Allura', cursive;
        letter-spacing: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(f'<p class="big-font">{val}</p>', unsafe_allow_html=True)

# Custom CSS for Yes/No buttons
st.markdown(
    """
    <style>
    div[class*="st-key-yes_maroon_btn"] button,
    div[class*="st-key-no_maroon_btn"] button {
        background-color: maroon;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render styled buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Yes", key="yes_maroon_btn", use_container_width=True):
        st.switch_page('pages/yes_page.py')
with col2:
    if st.button("No", key="no_maroon_btn", use_container_width=True):
        st.switch_page('pages/no_page.py')

# Hide video player controls using custom CSS
st.markdown(
    """
    <style>
    video::-webkit-media-controls {
        display: none !important;
    }
    video {
        -webkit-user-select: none;
        -webkit-touch-callout: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display your video (controls will be hidden)
st.video("videos/dfb.mp4", autoplay=True, muted=True, loop=True)


import base64

# Function to set background with image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    # Apply background using CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
            margin: 0;
            padding: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image
set_background("images/pinkheart.png")
