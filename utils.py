from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", 
                   openai_api_key = "sk-yhAcyxrDhcB7plE03a2e53D241954a64AcB61b6c40Ed5aA8",
                   openai_api_base = "https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("sk-yhAcyxrDhcB7plE03a2e53D241954a64AcB61b6c40Ed5aA8")))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("sk-yhAcyxrDhcB7plE03a2e53D241954a64AcB61b6c40Ed5aA8")))
