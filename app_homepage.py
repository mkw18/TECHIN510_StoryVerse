import streamlit as st

# Set page config
st.set_page_config(
    page_title="Storyverse", 
    layout="wide"
)

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
    if st.button('Start your Life Story'):
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
    st.markdown(f"**{user}** Welcome back! Your highest score in Lateral thinking puzzle is: **{score}**")
    level = st.selectbox("Level", ["Easy mode", "Challenge mode", "Difficult mode"])

    # Start button
    if st.button('Start Lateral Thinking Puzzle'):
        # Here you can add actions that occur when the Start button is pressed
        # For now, just display a simple message
        st.success("Puzzle started at level: " + level)
        # Add additional actions here, such as initializing puzzle game logic or redirecting to another page



st.subheader("Story Collection")

# Define your images, URLs, and descriptions in tuples
image_url_pairs = [
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/girl%20ocean.webp", "url_to_link_1", "Description for Girl Ocean"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/jungle%20boy.webp", "url_to_link_2", "Description for Jungle Boy"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/wealthy%20man.webp", "url_to_link_3", "Description for Wealthy Man"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/village%20girl.webp", "url_to_link_4", "Description for Village Girl"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/nightstory.webp", "url_to_link_5", "Description for Night Story"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/highheel.webp", "url_to_link_6", "Description for High Heel"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/field%20package.webp", "url_to_link_7", "Description for Field Package"),
    ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/ice.webp", "url_to_link_8", "Description for Ice"),
]

# Specify the fixed size for the images
image_size = "250px"  # You can change this to any size

# Create two rows with four columns each for the images
for i in range(0, len(image_url_pairs), 4):
    cols = st.columns(4)
    for col, (image_path, url, description) in zip(cols, image_url_pairs[i:i+4]):
        with col:
            # Display each image with a hover effect for the description
            hover_html = f"""
            <div style='position: relative; display: inline-block;'>
                <a href='{url}' target='_blank'>
                    <img src='{image_path}' style='height: {image_size}; width: {image_size}; object-fit: cover; border-radius: 5%;'>
                    <div style='position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); color: white; visibility: hidden; opacity: 0; transition: visibility 0s, opacity 0.5s ease; display: flex; justify-content: center; align-items: center; border-radius: 5%;'>
                        <div style='text-align: center; padding: 20px;'>{description}</div>
                    </div>
                </a>
                <script>
                    const container = document.currentScript.parentElement;
                    container.onmouseover = function() {{
                        container.children[1].children[1].style.visibility = 'visible';
                        container.children[1].children[1].style.opacity = '1';
                    }}
                    container.onmouseout = function() {{
                        container.children[1].children[1].style.visibility = 'hidden';
                        container.children[1].children[1].style.opacity = '0';
                    }}
                </script>
            </div>
            """
            st.markdown(hover_html, unsafe_allow_html=True)