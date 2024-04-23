import json

def add_tool_to_assistant(client, assistant_id):
    client.beta.assistants.update(
        assistant_id,
        tools=[file_search(), build_tool("tool_calling/get_tariffs.json")]
    )

def file_search():
    return {
        "type": "file_search"
    }
    
def build_tool(file_name):
    # Load Json and put in function
    func = json.load(open(file_name))
    func.pop("base_url")
    
    return {
        "type": "function",
        "function": func
        }
        

