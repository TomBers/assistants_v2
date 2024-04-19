from tool import get_tariffs
import json

def is_complete(run):
    return run.status == "complete" or run.status == "completed"

def get_result(client, thread):
    messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
    return messages.data[0].content[0].text.value
        
def get_tool_results(run):
    tool_outputs = []
    if run.required_action:
        for tool in run.required_action.submit_tool_outputs.tool_calls:
            if tool.function.name == "get_tariffs":
                function = tool.function
                arguments = json.loads(function.arguments)
                postcode = arguments['postcode']
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": json.dumps(get_tariffs(postcode))
                })
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