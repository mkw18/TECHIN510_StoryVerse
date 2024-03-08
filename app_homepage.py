import streamlit as st

# Set page config
st.set_page_config(page_title="Storyverse", layout="wide")

# Using HTML and CSS for background image in title and subheader
# Using HTML and CSS for a shared background image for title and subheader
st.markdown(
    """
    <style>
    .bg-section {
        background-image: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366');
        background-size: cover;
        padding: 50px;
        text-align: center;
        color: white; /* Change text color here if needed */
    }
    </style>
    <div class="bg-section">
        <h1>Storyverse</h1>
        <h2>Begin your journey in Storyverse...</h2>
    </div>
    """,
    unsafe_allow_html=True,
)


# Tabs centered workaround
tab1, tab2 = st.tabs(["Lifestory Simulator", "Lateral Thinking Puzzle"])

with tab1:
    # Add your content for Lifestory Simulator here
    st.write("Lifestory Simulator content goes here.")

with tab2:
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

