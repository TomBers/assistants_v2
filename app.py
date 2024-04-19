import chainlit as cl
from openai import OpenAI
from vector_store import retrieve_vector_store, file_upload, add_file_to_vector_store
from runs import is_complete, get_result, get_tool_results, submit_tool_outputs


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
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message.content
    )
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Plase answer any questions the user may have about their energy bill.  You have access to a tool that will return other available energy tariffs with which to make a comparision.",
        timeout=10.0
    )
    
    if is_complete(run):
        await cl.Message(content=get_result(client, thread)).send()
            
    # Check for tool_calls
    tool_outputs = get_tool_results(run)
    if tool_outputs:
        run = submit_tool_outputs(client, thread, run, tool_outputs)
        if is_complete(run):
            await cl.Message(content=get_result(client, thread)).send()
        
       
@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")
    
if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)