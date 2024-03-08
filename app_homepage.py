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

with tabs[0]:
    # Add your content for Lifestory Simulator here
    st.write("Lifestory Simulator content goes here.")
    

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

