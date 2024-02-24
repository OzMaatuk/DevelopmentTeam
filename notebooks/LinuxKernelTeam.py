import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

def termination_msg(msg):
        content = msg.get("content")
        if content.lower() in ("exit", "quit", "stop", "done", "terminate"):
            return True
        return False

def retrieve_content(message, n_results=3):
        ragassistant.n_results = n_results  # Set the number of results to be retrieved.
        # Check if we need to update the context.
        update_context_case1, update_context_case2 = ragassistant._check_update_context(message)
        if (update_context_case1 or update_context_case2) and ragassistant.update_context:
            ragassistant.problem = message if not hasattr(ragassistant, "problem") else ragassistant.problem
            _, ret_msg = ragassistant._generate_retrieve_user_reply(message)
        else:
            ret_msg = ragassistant.generate_init_message(message, n_results=n_results)
        return ret_msg if ret_msg else message


rag_path="rag\\Linux"
config_file="CONFIG_LIST.json"
filter_dict = {"model": ["gemini"]}
config_list = autogen.config_list_from_json(
    env_or_file=config_file, filter_dict=filter_dict
    )

llm_config = {
    "functions": [
        {
            "name": "retrieve_content",
            "description": "retrieve content for code generation and question answering.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",
                    }
                },
                "required": ["message"],
            },
        },
    ],
    "config_list": config_list,
    "timeout": 120,
    "seed": 50,
}

manager_llm_config = {
    "config_list": config_list,
    "timeout": 120,
    "seed": 50,
}

prompt1 = open("prompts/KernelGuru.txt").read()
prompt2 = open("prompts/PatchPro.txt").read()

ragassistant = RetrieveUserProxyAgent(
    name="Rag_Assistant",
    is_termination_msg=termination_msg,
    system_message="""Assistant who has extra content retrieval power for solving difficult problems.""",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
    retrieve_config={
        "task": "qa",
        "docs_path": rag_path
    },
)

agent1 = RetrieveAssistantAgent(
    name="Kernel_Guru",
    is_termination_msg=termination_msg,
    system_message=prompt1,
    llm_config=llm_config,
    human_input_mode="TERMINATE",
)


agent2 = RetrieveAssistantAgent(
    name="PatchPro",
    is_termination_msg=termination_msg,
    system_message=prompt2,
    llm_config=llm_config,
    human_input_mode="TERMINATE",
)

for agent in [agent1, agent2]:
    # register functions for all agents.
    agent.register_function(
        function_map={
            "retrieve_content": retrieve_content,
        }
    )

groupchat = autogen.GroupChat(
    agents=[agent1, agent2],
    messages=[],
    max_round=12,
    speaker_selection_method="round_robin",

)

task = open("prompts/task.txt").read()
coordinator = autogen.GroupChatManager(groupchat=groupchat, llm_config=manager_llm_config)
# Start chatting with the boss as this is the user proxy agent.
coordinator.initiate_chat(
    coordinator,
    message=task
)