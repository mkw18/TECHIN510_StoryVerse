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
    level = st.radio("Level", ["Easy mode", "Challenge mode", "Difficult mode"])
    # You can add additional content or interactive elements for the puzzle here

# Story collection section
st.subheader("Story Collection")
# Layout for stories, assuming 4 stories per row as an example
cols = st.columns(6)
for i in range(6):  # Assuming we have 4 stories, you can adjust this number
    with cols[i]:
        # Placeholder or actual content for each story
        st.image("files\img\girl ocean.webp", caption="Title or Date")  # Replace with actual path and title
        # Add interactivity or details for each story

