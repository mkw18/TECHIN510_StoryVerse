from tempfile import NamedTemporaryFile
import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE'))

# st.set_page_config(
#     page_title="Story Verse",
#     page_icon="🐢",
#     layout="centered",
#     initial_sidebar_state="auto",
#     menu_items=None,
# )
st.set_page_config(layout="wide")
left_sidebar, main_content, right_sidebar = st.columns([1, 4, 1])

# Sidebar
with left_sidebar:
    st.header("Menu")
    st.button("Restart")
    st.button("Pause")

rules = "1. 你知道汤面和汤底，当用户需要玩海龟汤时，给予用户汤面，用户只知道汤面，不知道汤底。\n2. 用户提出可以用“是”、“否”、“无关”来回答的问题，用户提问是为了猜测到汤底，你根据汤底回答用户的提问，只能用“是”、“否”或“无关”回答用户，从而引导用户猜到正确的汤底。\n3. 如果用户直接以“为什么”的形式询问汤面的细节，请告知用户需要自己猜测。\n4. 你要充分理解和准确解读汤底的信息，根据汤底的信息和用户过往提问信息对用户的提问做出回答，用户的提问不一定包含汤底的信息，但是你的回答必须符合汤底的事实。\n5. 只有在汤底无法提供直接或间接的答案时，你才可以回答“无关”，注意这是回答“无关”的唯一条件，其他时候你要回答“是”或“否”。\n6. 你不能直接将汤底的信息告诉用户，就算用户直接问也不行。\n7. 要整体判断用户的提问，理解用户整体的意思，不可片面通过某一个点作答，所答必须符合汤底事实。\n8. 当用户在猜测汤底的过程中，猜到部分真相但与汤底的完整真相还有差距时，你可以提供一定的切入点提示，但不能直接透露汤底的信息。"
prim_prompt = f"我需要你做一个游戏的主持人，游戏名叫海龟汤。\n\n海龟汤游戏由汤面和汤底组成，你的汤面是：“{story}”\n你的汤底是：“{answer}”\n\n游戏规则：\n{rules}\n\n游戏过程中，请你用以上游戏规则约束你的行为，因为这样可以为用户带来良好的游戏体验。仔细审题，确保回答符合游戏规则和汤底的信息，当用户发出游戏请求时，给出汤面，并通过回答“是”、“否”或“无关”帮助用户猜到汤底。注意每次回答你都必须确保自己充分理解并遵守了以上游戏规则和你的汤面及汤底，保证用户体验，不要出现无法回答的情况，更不要违反游戏规则。"

hosting = [
    {"role": "user", "content": prim_prompt},
    {"role": "assistant", "content": "好的，我明白自己的角色是海龟汤游戏的主持人，要通过回答用户的问题帮助用户猜到汤底。我已充分理解汤面和汤底的所有信息，并认真阅读了所有规则，保证自己会在游戏过程中遵守所有规则。"},
    {"role": "user", "content": "请总结汤面的关键点，以确保你理解了汤面。"},
    {"role": "assistant", "content": story_key},
    {"role": "user", "content": "请总结汤底的关键点，以确保你理解了汤底。"},
    {"role": "assistant", "content": answer_key},
    {"role": "user", "content": "请复述一遍规则，以确保你理解了所有规则。"},
    {"role": "assistant", "content": rules},
    {"role": "user", "content": "好的，我们现在可以开始游戏了。记住，每次回答前你要回顾汤面的关键点、汤底的关键点、规则，回答是或否或无关。"},
    {"role": "assistant", "content": f"好的，作为游戏的主持人，我将遵守以上规则，并确保回答符合规则和汤底的信息。下面是你的汤面：\n{story}\n\n你可以开始猜测汤底的内容，我会回答你的问题。请注意，你的问题需要能够用“是”、“否”或“无关”来回答。"},
]

with main_content:
    st.markdown("<h1 style='text-align: center; color: black;'>Lateral Thinking Puzzle</h1>", unsafe_allow_html=True)
    if "messages" not in st.session_state.keys():  # Initialize the chat messages history
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome to Lateral Thinking Puzzle!"}
        ]

if prompt := st.chat_input(
    "Your question"
):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

with main_content:
    for message in st.session_state.messages:  # Display the prior chat messages
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

# Scoreboard
with right_sidebar:
    st.header("Scoreboard")
    scoreboard_placeholder = st.empty()
    scoreboard_placeholder.text("This is a placeholder for the scoreboard")

