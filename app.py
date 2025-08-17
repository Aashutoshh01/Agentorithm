import streamlit as st
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio

st.title("Agentorithm")
st.write("Agentorithm is an agentic AI system that collaborates to solve Data Structures and Algorithms problems efficiently in Python.")

task=st.text_input("Enter your DSA query.",value="write a function to add two numbers")

async def run(team,docker,task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg:=f"{message.source}:{message.content}")
                yield msg
            elif isinstance(message,TaskResult):
                print(msg:=f"Stop Reason:{message.stop_reason}")
                yield msg
        print("Task Completed")
    except Exception as e:
        print(f"Error:{e}")
        yield f"Error:{e}"
    finally:
        await start_docker_container(docker)

if st.button("Run"):
    st.write("Fetching...")
    team,docker=get_dsa_team_and_docker()

    async def collect_message():
        async for msg in run(team,docker,task):
            if isinstance(msg,str):
                if msg.startswith("user"):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith('DSA_Problem_Solver_Agent'):
                    with st.chat_message('assistant',avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith('CodeExecutorAgent'):
                    with st.chat_message('assistant',avatar='🤖'):
                        st.markdown(msg)
            elif isinstance(msg,TaskResult):
                with st.chat_message('stopper',avatar='🚫'):
                    st.markdown(f"Task Completed: {msg.result}")

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(collect_message())

    #asyncio.run(collect_message())

st.markdown("---")
st.caption("🚀 Created by **Aashutosh Joshi**")