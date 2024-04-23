from tool_utils import extract_parameter_names

def build_thread(client, vector_store):
    return client.beta.threads.create(
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store.id]
                }
            }
        )
    
def run_thread(client, thread, assistant, instructions, timeout=10.0):
    return client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions=instructions,
        timeout=timeout
    )
    
def build_tool_instruction():
    # Write a function that opens a json file called get_tariffs.json and extract out the names of all parmeters
    parameter_names = extract_parameter_names('tool_calling/get_tariffs.json')
    inst = "From the uploaded document please extract these key parameters: "
    for p in parameter_names:
        inst += f"{p}, "
    return inst

    
print(build_tool_instruction())