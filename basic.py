from swarm import Swarm, Agent
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = Swarm()

# CSS test
st.markdown(
    """
    <style>
    .chat-section-tools {
        color: black;
        background-color: #f5f5f5; /* Change this to your desired color */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .chat-section h5 {
        margin: 0;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .chat-section-assistant {
        color: black;
        background-color: green; /* Change this to your desired color */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: right;
    }
    .chat-section h5 {
        margin: 0;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Swarm Tutorial")

def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="agent A",
    instructions="You are a helpful agent",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="agent B",
    instructions="Only speak in Haikus. and writes a haiku for the user.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
    debug=True,
)

# print(response.messages[-1]["content"])
st.json(response.messages, expanded=False)

for message in response.messages:
    if message["role"] == "user":
        if message["content"]:
            with st.chat_message("User"):
                st.markdown(f"""<div class="chat-section"> <h5>User:</h5>{message['content']}</div>""", unsafe_allow_html=True)
    elif message["role"] == "assistant":
        if message["content"]:
            with st.container():
                st.markdown(f"""<div class="chat-section-assistant"> <h5>Assistant:</h5>{message['content']}</div>""", unsafe_allow_html=True)
    elif message["role"] == "tool":
        if message["content"]:
            with st.container():
                st.markdown(f"""<div class="chat-section-tools"> <h5>Tools:</h5>{message['tool_name']}</div>""", unsafe_allow_html=True)
                
for message in response.messages:
    if message["role"] == "user":
        if message["content"]:
            with st.chat_message("User"):
                st.markdown(f"""<div class="chat-section"> <h5>User:</h5>{message['content']}</div>""", unsafe_allow_html=True)
    elif message["role"] == "assistant":
        if message["content"]:
            with st.container():
                st.markdown(f"""<div class="chat-section-assistant"> <h5>Assistant:</h5>{message['content']}</div>""", unsafe_allow_html=True)
    elif message["role"] == "tool":
        if message["content"]:
            with st.container():
                st.markdown(f"""<div class="chat-section-tools"> <h5>Tools:</h5>{message['tool_name']}</div>""", unsafe_allow_html=True)
                
