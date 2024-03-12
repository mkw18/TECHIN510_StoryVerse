import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE'))

# st.set_page_config(layout="wide")

def ls_page(gender, family, parent, live, siblings):
    def new_game():
        hosting = [
            {
                "role": "system",
                "content": "Imagine you're a game host of a life simulation game, where you guide players through 3-4 different life story development paths starting from birth (age: 0). Based on the choices made, different story developments will unfold. Additionally, players may face random events that could have positive or negative impacts, altering their life's course.\n\n"
                "Before the story begins, you will sequentially ask the user about their:\n\n"
                "Gender:\n"
                "Male/Female\n"
                "Family:\n"
                "modest family/wealthy family/rural family/international family\n"
                "Parents' relationship:\n"
                "happy and prosperous/Divorced but friendly/Tension and conflict/One of them died young/Unmarried children\n"
                "Living in:\n"
                "Prosperous City/Small Town Community/Rural countryside/Small fishing village by the sea/Mountain Jungle\n"
                "Siblings:\n"
                "0/1/2/3\n"
                "After each round of choices and story generation, update the following attributes with specific values, such as looks: 95, cash: 1021. Display all values only after they are updated.\n\n"
                "Age\n"
                "Looks\n"
                "Cash\n"
                "Intelligence\n"
                "Health\n"
                "Mood\n"
                "Please present your answer in the following format:\n"
                "Attributes\n"
                "Age: some value\n"
                "Looks: some value\n"
                "Cash: some value\n"
                "Intelligence: some value\n"
                "Health: some value\n"
                "Mood: some value\n"
                "Story\n"
                "(your story here)\n"
                "Choice\n"
                "(list the event or path choice here)"
            },
            {
                "role": "assistant",
                "content": "Let's embark on an intriguing journey through the life simulation game. Before we dive into your unique story, please make the following choices to set the stage for your life's path:"
                "Gender: Male / Female"
                "Family Background: Modest Family / Wealthy Family / Rural Family / International Family"
                "Parents' Relationship: Happy and Prosperous / Divorced but Friendly / Tension and Conflict / One of Them Died Young / Unmarried Children"
                "Living Environment: Prosperous City / Small Town Community / Rural Countryside / Small Fishing Village by the Sea / Mountain Jungle"
                "Siblings: 0 / 1 / 2 / 3"
            },
            {
                "role": "user",
                "content": f"{gender}, {family}, {parent}, {live}, {siblings}",
            }
        ]
        st.session_state.messages = hosting

    left_sidebar, main_content, right_sidebar = st.columns([2, 4, 1])

    # Sidebar
    with left_sidebar:
        st.header("Story")
        st.button("Re-generate", on_click=new_game)
        st.session_state.stroy_txt = st.empty()

    # Scoreboard
    with right_sidebar:
        st.header("Attributes")
        st.session_state.attributes = st.empty()

    with main_content:
        st.markdown("<h1 style='text-align: center; color: black;'>Life Story Simulator</h1>", unsafe_allow_html=True)
        if "messages" not in st.session_state.keys():  # Initialize the chat messages history
            new_game()

    if prompt := st.chat_input(
        "Your choice"
    ):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.attributes.text_area('Attributes', value=st.session_state.attr, height=300, disabled=True)
        st.session_state.stroy_txt.text_area('Story', value=st.session_state.story, height=400, disabled=True)

    with main_content:
        for message in st.session_state.messages[3:]:  # Display the prior chat messages
            with st.chat_message(message["role"]):
                if message["role"] == "assistant":
                    st.write(message["content"].split('Choice')[1].strip())
                else:
                    st.write(message["content"])
        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    completion = client.chat.completions.create(
                        model="gpt-4",
                        messages=st.session_state.messages
                    )
                    response = completion.choices[0].message.content
                    print(response)
                    attribute = response.split("Attributes")[-1]
                    attribute, story = attribute.split('Story')[0].strip(), attribute.split('Story')[1].strip()
                    story, choice = story.split('Choice')[0].strip(), story.split('Choice')[1].strip()
                    if attribute[0] == ':':
                        attribute = attribute[1:].strip()
                    if story[0] == ':':
                        story = story[1:].strip()
                    if choice[0] == ':':
                        choice = choice[1:].strip()
                    st.session_state.attributes.text_area('Attributes', value=attribute, height=300, disabled=True)
                    st.session_state.stroy_txt.text_area('Story', value=story, height=400, disabled=True)
                    st.session_state.attr = attribute
                    st.session_state.story = story
                    st.write(choice)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)  # Add response to message history

ls_page("Male", "Modest Family", "Happy and Prosperous", "Prosperous City", 0)