import streamlit as st

# Title of your app
st.title(":blue[Sultan IT Web & Generative AI]")

# Header
st.header(":rainbow[So much we can build here on streamlit!]")

# Subheader
st.subheader(":green[Hello I'm Sultan Ahmed]")
st.image("./1.png", width=300)

# Regular text
st.write("Welcome to my Streamlit practice!")

if st.button(":green[Send balloons!]"):
    st.balloons()

# Using Markdown for formatted text
st.markdown("222---333[ABC]")  # Horizontal line
st.markdown("**This text is bold.**")
st.markdown("*This text is italicized.*")
st.markdown("You can also create lists:")
st.markdown("- Item 1")
st.markdown("- Item 2")
st.markdown("Or use LaTeX for equations: $E=mc^2$")

# Displaying code
st.code("import streamlit as st\nst.write('Hello')", language="python")

# Success, info, warning, error messages
st.success("This is a success message!")
st.info("This is an informational message.")
st.warning("This is a warning message.")
st.error("This is an error message.")

st.title("Interactive Elements")

# Button
if st.button("Click Me"):
   st.write("You clicked the button!")

# Text Input
name = st.text_input("Enter your name:", "Type here...")
if name:
       st.write(f"Hello, {name}!")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=150, value=25, step=1)
st.write(f"You are {age} years old.")

# Checkbox
agree = st.checkbox("I agree to the terms and conditions.")
if agree:
    st.write("Thank you for agreeing!")

# Radio Buttons
option = st.radio("Select an option:", ("Option A", "Option B", "Option C"))
st.write(f"You selected: {option}")

# Select Box (Dropdown)
favorite_color = st.selectbox("Choose your favorite color:", ("Red", "Green", "Blue", "Yellow"))
st.write(f"Your favorite color is: {favorite_color}")

# Slider
number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected: {number}")

st.title("Layout Practice")

# Sidebar
with st.sidebar:
    st.header(":blue[FaizanMedico]")
    name = st.text_input("Your name:", "Guest")
    slider_value = st.slider("Select a value for the main area:", 0, 100, 25)
    st.write(f"Hello from the sidebar, {name}!")

st.subheader("Main Area")
st.write(f"The value selected in the sidebar is: {slider_value}")

st.subheader("Using Columns")
col1, col2 = st.columns(2)

with col1:
    st.info("This is the first column.")
    st.write("Some content here...")

with col2:
    st.warning("This is the second column.")
    st.slider("Slider in column 2:", 0, 50, 10)

st.subheader("More Columns (Unequal Widths)")
col3, col4, col5 = st.columns([1, 2, 1])  # Width ratios

with col3:
    st.success("Col 3 (width 1)")
with col4:
    st.error("Col 4 (width 2)")
with col5:
    st.info("Col 5 (width 1)")





from PIL import Image
import requests
from io import BytesIO

st.title("Displaying Media")
st.audio_input("Record a voice message")

st.subheader("Displaying an Image from Local File:")
try:
    image = Image.open("streamlit_logo.png")  # Make sure you have this image in the same directory
    st.image(image, caption="Streamlit Logo", width=300)
except FileNotFoundError:
    st.error("Please make sure 'streamlit_logo.png' is in the same directory.")

st.subheader("Displaying an Image from URL:")
image_url = "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
st.image(img, caption="Streamlit Logo from URL", width=200)
st.image("./1.png", width=200)


st.subheader("Displaying Audio (if you have an audio file):")
# Replace 'audio.mp3' with the path to your audio file
# try:
#     audio_file = open('audio.mp3', 'rb')
#     audio_bytes = audio_file.read()
#     st.audio(audio_bytes, format='audio/mp3')
# except FileNotFoundError:
#     st.info("Place an 'audio.mp3' file in the same directory to test audio.")


st.subheader("Displaying Video (if you have a video file):")
# Replace 'video.mp4' with the path to your video file
# try:
#     video_file = open('video.mp4', 'rb')
#     video_bytes = video_file.read()
#     st.video(video_bytes)
# except FileNotFoundError:
#     st.info("Place a 'video.mp4' file in the same directory to test video.")

st.camera_input("Take a picture")
st.color_picker("Pick a color")



st.markdown(
    """
    <style>
    .custom-container {
        background-color: #e0f7fa; /* Light blue */
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="custom-container">', unsafe_allow_html=True)
st.subheader("Section Title")
st.write("Content within the custom container.")
st.markdown('</div>', unsafe_allow_html=True)

st.write("Content outside the container.")

st.image("./1b.png", width=300)
st.image("./1a.png", width=600)






import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-image: url("your_image.jpg"); /* Replace with your image path/URL */
        background-size: cover; /* Adjust as needed: contain, auto, etc. */
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Streamlit App with Background Image")
st.write("More content...")






import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6; /* Light gray */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("My Streamlit App with Custom Background")
st.write("Some content here...")


