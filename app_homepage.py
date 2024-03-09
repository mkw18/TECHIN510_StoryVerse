import streamlit as st

# Set page config
st.set_page_config(page_title="Storyverse", layout="wide")

# Using HTML and CSS for background image in title and subheader
st.markdown(
    """
    <style>
    .bg-section {
        background-image: url('https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/background.webp');
        background-size: cover;
        padding: 50px;
        text-align: center;
        color: white; /* Change text color here if needed */
    }
    </style>
    <div class="bg-section">
        <h1 style="color: white;">Storyverse</h1>
        <h2 style="color: white;">Begin your journey in Storyverse...</h2>
    </div>
    """,
    unsafe_allow_html=True,
)


# Initialize tab labels and the amount of whitespace
listTabs = ["Lifestory Simulator", "Lateral Thinking Puzzle"]
whitespace = 65



## Fills and centers each tab label with em-spaces
tabs = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

# Using the first tab for Lifestory Simulator
with tabs[0]:  
    # Defining the choices for the user
    gender = st.selectbox("Gender:", ('Male', 'Female'))
    family = st.selectbox("Family:", ('Modest family', 'Wealthy family', 'Rural family', 'International family'))
    parents_relationship = st.selectbox("Parents' relationship:", ('Happy and prosperous', 'Divorced but friendly', 'Tension and conflict', 'One of them died young', 'Unmarried children'))
    live_in = st.selectbox("Live in:", ('Prosperous city', 'Small town community', 'Rural countryside', 'Small fishing village by the sea', 'Mountain jungle'))
    siblings = st.selectbox("Siblings:", ('0', '1', '2', '3'))

    # Start button
    if st.button('Start'):
        # You can replace 'url_to_gamepage' with the actual URL or path to your game page
        # For example, you can display a message, redirect to another page, or start the game simulation based on the user's choices
        st.success("Starting the game...")
        # Redirect to the game page or initiate the game scenario
        # For demonstration, we just print the choices
        st.write(f"Selected options: Gender: {gender}, Family: {family}, Parents' relationship: {parents_relationship}, Live in: {live_in}, Siblings: {siblings}")
        # In actual application, you might redirect or start simulation here
    

with tabs[1]:
    # Add your content for Lateral Thinking Puzzle here
    st.write("Lateral Thinking Puzzle content goes here.")
    user = "@Mkw24"
    score = 85  # Assuming this is fetched or calculated somehow
    st.markdown(f"**{user}** Welcome back! your highest score in Lateral thinking puzzle is: **{score}**")
    level = st.selectbox("Level", ["Easy mode", "Challenge mode", "Difficult mode"])
    # You can add additional content or interactive elements for the puzzle here

st.subheader("Story Collection")

# Define your images and URLs in pairs
# Replace 'path_to_image' with your actual image paths and 'url_to_link' with the actual URLs
image_url_pairs = [
    ("path_to_image_1", "url_to_link_1"),
    ("path_to_image_2", "url_to_link_2"),
    ("path_to_image_3", "url_to_link_3"),
    ("path_to_image_4", "url_to_link_4"),
    ("path_to_image_5", "url_to_link_5"),
    ("path_to_image_6", "url_to_link_6"),
    ("path_to_image_7", "url_to_link_7"),
    ("path_to_image_8", "url_to_link_8"),
]

# Create two rows with four columns each for the images
for i in range(0, len(image_url_pairs), 4):
    cols = st.columns(4)
    for col, (image_path, url) in zip(cols, image_url_pairs[i:i+4]):
        with col:
            # Display each image using Markdown to make it clickable
            st.markdown(f"[![image]({image_path})]({url})", unsafe_allow_html=True)
            # You can add captions or other text below each image as needed

