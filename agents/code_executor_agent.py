from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_executor import get_docker_executor

def get_code_executor_agent():
    docker=get_docker_executor()
    code_executor_agent=CodeExecutorAgent(
        name='CodeExecutorAgent',
        code_executor=docker
    )
    return code_executor_agent,docker
