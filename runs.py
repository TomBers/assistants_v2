import json
from test_http_approach import run_req


def is_complete(run):
    return run.status == "complete" or run.status == "completed"

def run_tool(tool):
    tool_func = tool.function
    
    if isinstance(tool_func.arguments, str):
        # Convert the string to a dictionary
        arguments = json.loads(tool_func.arguments)
    else:
        # If it's already a dictionary, use it as is
        arguments = tool_func.arguments
        
    return {
            "tool_call_id": tool.id,
            "output": json.dumps(run_req(arguments))
            }

def get_result(client, thread):
    messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
    return messages.data[0].content[0].text.value
        
def get_tool_results(run):
    tool_outputs = []
    if run.required_action:
        for tool in run.required_action.submit_tool_outputs.tool_calls:
            tool_outputs.append(run_tool(tool))
    return tool_outputs


def submit_tool_outputs(client, thread, run, tool_outputs):
    try:
        return client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
        
    except Exception as e:
        print("Failed to submit tool outputs:", e) 