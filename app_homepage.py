import streamlit as st
from app_ltp import ltp_page
from app_ls import ls_page

# Set page config
st.set_page_config(
    page_title="Storyverse", 
    layout="wide"
)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name

if st.session_state.page == 'ltp':
    ltp_page(st.session_state.level)

elif st.session_state.page == 'ls':
    ls_page(st.session_state.gender, st.session_state.family, st.session_state.parents_relationship, st.session_state.live_in, st.session_state.siblings)

else:
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
        st.session_state.gender = st.selectbox("Gender:", ('♂️Male', '♀️Female'))
        st.session_state.family = st.selectbox("Family:", ('Modest family', 'Wealthy family', 'Rural family', 'International family'))
        st.session_state.parents_relationship = st.selectbox("Parents' relationship:", ('Happy and prosperous', 'Divorced but friendly', 'Tension and conflict', 'One of them died young', 'Unmarried children'))
        st.session_state.live_in = st.selectbox("Live in:", ('🌇Prosperous city', '🏘️Small town', '🛖Rural countryside', '🌊fishing village', '⛰️Mountain jungle'))
        st.session_state.siblings = st.selectbox("Siblings:", ('0', '1', '2', '3'))

        # Start button
        if st.button('Start your Life Story', on_click=go_to_page, args=('ls',)):
            # You can replace 'url_to_gamepage' with the actual URL or path to your game page
            # For example, you can display a message, redirect to another page, or start the game simulation based on the user's choices
            st.success("Starting the game...")
            # Redirect to the game page or initiate the game scenario
        

    with tabs[1]:
        # Add your content for Lateral Thinking Puzzle here
        st.write("Lateral Thinking Puzzle content goes here.")
        user = "@Mkw24"
        score = 85  # Assuming this is fetched or calculated somehow
        # st.markdown(f"**{user}** Welcome back! Your highest score in Lateral thinking puzzle is: **{score}**")
        level = st.selectbox("Level", ["⭐Easy mode", "⭐⭐Challenge mode", "⭐⭐⭐Difficult mode"])
        level_LUT = {"⭐Easy mode": 'easy', "⭐⭐Challenge mode": 'medium', "⭐⭐⭐Difficult mode": 'hard'}
        st.session_state.level = level_LUT[level]

        # Start button
        if st.button('Start Lateral Thinking Puzzle', on_click=go_to_page, args=('ltp',)):
            # Here you can add actions that occur when the Start button is pressed
            # For now, just display a simple message
            st.success("Puzzle started at level: " + level)
            # Add additional actions here, such as initializing puzzle game logic or redirecting to another page



    st.subheader("Story Collection")

    # Define your images, URLs, and descriptions in tuples
    # Add a third element to each tuple for the description
    image_url_descriptions = [
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/girl%20ocean.webp", "url_to_link_1", "Lifestory:Girl by the Ocean"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/jungle%20boy.webp", "url_to_link_2", "Lifestory:Jungle Boy"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/wealthy%20man.webp", "url_to_link_3", "Lifestory:Born with a golden spoon"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/village%20girl.webp", "url_to_link_4", "Lifestory:Village Girl"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/nightstory.webp", "url_to_link_5", "Puzzle:Night Story"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/highheel.webp", "url_to_link_6", "Puzzle:High Heel"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/field%20package.webp", "url_to_link_7", "Puzzle:Field Package"),
        ("https://raw.githubusercontent.com/mkw18/TECHIN510_StoryVerse/main/files/img/ice.webp", "url_to_link_8", "Puzzle:Ice"),
    ]

    # Specify the fixed size for the images
    image_size = "300px"  # You can change this to any size

    # Create two rows with four columns each for the images
    for i in range(0, len(image_url_descriptions), 4):
        cols = st.columns(4)
        for col, (image_path, url, description) in zip(cols, image_url_descriptions[i:i+4]):
            with col:
                # Display each image with a description below it
                markdown_html = f"""
                <a href='{url}' target='_blank'>
                    <img src='{image_path}' style='height: {image_size}; width: {image_size}; object-fit: cover; border-radius: 5%;'>
                </a>
                <p style='text-align: left;'>{description}</p>
                """
                st.markdown(markdown_html, unsafe_allow_html=True)
