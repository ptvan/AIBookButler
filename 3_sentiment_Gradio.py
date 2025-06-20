import gradio as gr
from langchain.schema import AIMessage, HumanMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

def predict(message, history):
    history_langchain_format = []
    for msg in history:
        if msg['role'] == "user":
            history_langchain_format.append(HumanMessage(content=msg['content']))
        elif msg['role'] == "assistant":
            history_langchain_format.append(AIMessage(content=msg['content']))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = model.invoke(history_langchain_format)
    return gpt_response.content

demo = gr.ChatInterface(
    predict,
    type="messages"
)

demo.launch()