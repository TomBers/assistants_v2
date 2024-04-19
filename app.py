import chainlit as cl
from openai import OpenAI
from vector_store import retrieve_vector_store, file_upload, add_file_to_vector_store


@cl.on_chat_start
async def start():
    assisant_id = "asst_N9HxBMtsKvnsfPDvg9muOjjn"   
    client = OpenAI()
    assistant = client.beta.assistants.retrieve(assisant_id)
    vector_store = retrieve_vector_store(client)
    
    thread = client.beta.threads.create(
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store.id]
                }
            }
        )
    
    # print(thread)
    
    cl.user_session.set("client", client)
    cl.user_session.set("assistant", assistant)
    cl.user_session.set("thread", thread)
    cl.user_session.set("vector_store", vector_store)
    

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
    
    client = cl.user_session.get("client")
    vector_store = cl.user_session.get("vector_store")
    thread = cl.user_session.get("thread")
    assistant = cl.user_session.get("assistant")
    
    if message.elements:
        for element in message.elements:
            file_object = file_upload(client, element)
            vsf = add_file_to_vector_store(client, vector_store, file_object)
            print(vsf)
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message.content
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe."
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        res = messages.data[0].content[0].text.value
        print(res)
        await cl.Message(content=res).send()
    else:
        return run.status
        
@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")
    
if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)