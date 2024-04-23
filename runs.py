import json
import importlib
import sys

sys.path.append('tool_calling')

def is_complete(run):
    return run.status == "complete" or run.status == "completed"

def run_tool(tool):
    tool_func = tool.function
    func = getattr(importlib.import_module(tool_func.name), tool_func.name)
    res = func(**tool_func.arguments)
    return {
                "tool_call_id": tool.id,
                "output": json.dumps(res)
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