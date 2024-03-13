import os
import random
import streamlit as st
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE'))

# st.set_page_config(layout="wide")

def ltp_page(level):
    def show_hide_answer():
        with left_sidebar:
            st.session_state.stroy_txt = st.empty()
            st.session_state.stroy_txt.text_area('Story', value=st.session_state.story, height=299, disabled=True)
        with right_sidebar:
            st.session_state.scoreboard_placeholder = st.empty()
            st.session_state.scoreboard_placeholder.text(f'💖 {st.session_state.likes}\n⏰ {st.session_state.time}\n⭐ {st.session_state.q_level}\n🗓 {st.session_state.date}')
            st.session_state.answer_txt = st.empty()
            if st.session_state.show_answer:
                st.session_state.answer_txt.text_area('Answer', value='', height=299, disabled=True)
            else:
                st.session_state.answer_txt.text_area('Answer', value=st.session_state.answer, height=299, disabled=True)
            st.session_state.show_answer = not st.session_state.show_answer

    def on_restart():
        st.session_state.messages = st.session_state.messages[:10]
        st.session_state.show_answer = True
        show_hide_answer()

    def new_game():
        line = json.loads(lines[st.session_state.index])
        story, answer, story_keys, answer_keys = line['story'][0], line['answer'][0], line['story_keys'], line['answer_keys']
        st.session_state.scoreboard_placeholder.text(f'💖 {line["likes"]}\n⏰ {line["solving_time"]}\n⭐ {line["level"]}\n🗓 {line["date"]}')
        st.session_state.stroy_txt.text_area('Story', value=story, height=300, disabled=True)
        st.session_state.answer_txt.text_area('Answer', value='', height=300, disabled=True)
        hosting = [
            {
                "role": "system",
                "content": f"I need you to be the host of a game called Lateral Thinking Puzzle.\n\nLateral Thinking "
                f"Puzzle is a game consist of a story and a truth. Your story is: '{story}'\nYour t"
                f"ruth is: '{answer}'\n\nHere are the game rules:\n{rules}\n\nDuring the game "
                f"process, please adhere to the above game rules to ensure a positive gaming experience "
                f"for the users. Pay close attention to the questions asked and ensure that your responses "
                f"comply with both the game rules and the information from the truth. When a user requests "
                f"to play the game, provide them with the story and help them guess the truth by answering "
                f'with "yes", "no", or "irrelevant". Remember that with each response, you must fully '
                f"understand and abide by the aforementioned game rules, as well as the story and the "
                f"truth. This will ensure a smooth user experience and avoid situations where you cannot "
                f"answer or violate the game rules.",
            },
            {
                "role": "assistant",
                "content": "Alright, I understand that my role is to be the host of the Lateral Thinking Puzzle and "
                "help users guess the truth by answering their questions. I have fully grasped all the "
                "information regarding the story and the truth and have carefully read all the rules. I "
                "assure that I will abide by all the rules throughout the game process.",
            },
            {
                "role": "user",
                "content": "Please summarize the key points of the story to ensure that you have understood it.",
            },
            {"role": "assistant", "content": story_keys},
            {
                "role": "user",
                "content": "Please summarize the key points of the truth to ensure that you have understood it.",
            },
            {"role": "assistant", "content": answer_keys},
            {
                "role": "user",
                "content": "Please restate the rules to ensure that you have understood all of them.",
            },
            {"role": "assistant", "content": rules},
            {
                "role": "user",
                "content": "Alright, we can now start the game. Remember, before each response, you should review the "
                'key points of the story, the key points of the truth, and the rules. Answer with "yes", '
                '"no", or "irrelevant".',
            },
            {
                "role": "assistant",
                "content": f"Alright, as the host of the game, I will adhere to the above rules and ensure that my "
                f"responses comply with the rules and the information from the truth. Below is your story: "
                f"\n{story}\n\nYou can start guessing the content of the truth, and I will answer your "
                f'questions. Please note that your questions should be answerable with "yes", "no", '
                f'or "irrelevant".',
            },
        ]
        st.session_state.messages = hosting
        st.session_state.index += 1
        st.session_state.story = story
        st.session_state.answer = answer
        st.session_state.likes = line["likes"]
        st.session_state.time = line["solving_time"]
        st.session_state.q_level = line["level"]
        st.session_state.date = line["date"]

    def on_new_game():
        new_game()
        st.session_state.show_answer = True
        show_hide_answer()

    left_sidebar, main_content, right_sidebar = st.columns([1, 4, 1])

    st.session_state.index = 0
    with open(f'data/{level}.json') as f:
        lines = f.readlines()
        random.shuffle(lines)

    # Sidebar
    with left_sidebar:
        st.header("Menu")
        st.button("Restart", on_click=on_restart)
        st.button("New Game", on_click=on_new_game)
        st.session_state.stroy_txt = st.empty()

    # Scoreboard
    with right_sidebar:
        st.header("Details")
        answer_btn = st.button('Show Answer', on_click=show_hide_answer)
        st.session_state.scoreboard_placeholder = st.empty()
        st.session_state.answer_txt = st.empty()

    rules = (
        '1. You know both the "story" and the "truth". When a user wants to play Lateral Thinking Puzzle, '
        'you provide them with the "story". The user only knows the "story" and is unaware of the '
        '"truth".\n2. The user asks questions that can be answered with "yes," "no," or "irrelevant". Their '
        'questions are aimed at guessing the "truth". Based on the "truth", you respond to the user\'s '
        'questions using "yes," "no," or "irrelevant" to guide them towards guessing the correct truth.\n3. '
        'If the user directly asks for details about the truth using the form of "why" questions, inform them '
        "that they need to make their own guesses.\n4. You must fully understand and accurately interpret the "
        "information from the truth. Based on the information of the truth and the user's past questions, "
        "you answer the user's questions. The user's questions may not necessarily contain information from "
        "the truth, but your responses must align with the facts of the truth.\n5. You can only answer "
        '"irrelevant" when the truth cannot provide a direct or indirect answer. Note that this is the only '
        'condition for responding "irrelevant"; otherwise, you should answer "yes" or "no."\n6. You cannot '
        "directly disclose the information from the truth to the user, even if they ask directly.\n7. You "
        "need to judge the user's questions as a whole and understand their overall intent. Avoid answering "
        "based solely on a particular point; your responses must align with the facts of the truth.\n8. "
        "During the user's process of guessing the truth, if they come close to some truths but still have "
        "gaps in understanding the complete truth of the truth, you can provide certain entry point hints. "
        "However, you cannot directly reveal information from the truth."
    )

    with main_content:
        st.markdown("<h1 style='text-align: center; color: black;'>Lateral Thinking Puzzle</h1>", unsafe_allow_html=True)
        if "messages" not in st.session_state.keys():  # Initialize the chat messages history
            new_game()
            st.session_state.show_answer = False

    if prompt := st.chat_input(
        "Your question"
    ):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.show_answer = not st.session_state.show_answer
        show_hide_answer()

    with main_content:
        with st.chat_message("assistant"):
            st.write(st.session_state.story)
        for message in st.session_state.messages[10:]:  # Display the prior chat messages
            with st.chat_message(message["role"]):
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
                    st.write(response)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)  # Add response to message history

# ltp_page('medium')