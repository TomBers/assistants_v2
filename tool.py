import json

def add_tool_to_assistant(client, assistant_id):
    client.beta.assistants.update(
        assistant_id,
        tools=[build_tool("tool_calling/get_quality_score.json"), build_tool("tool_calling/get_tariffs.json")]
    )
    
def build_tool(file_name):
    # Load Json and put in function
    func = json.load(open(file_name))
    return {
        "type": "function",
        "function": func
        }
        

def get_tariffs(postcode):
    print("get_tariffs called")
    print(postcode)
    return [
        {
            "name": "Tariff 1",
            "price": 100
        },
        {
            "name": "Tariff 2",
            "price": 200
        },
        {
            "name": "Tariff 3",
            "price": 300
        }
    ]