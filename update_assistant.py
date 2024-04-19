from openai import OpenAI
from tool import add_tool_to_assistant

client = OpenAI()

assisant_id = "asst_N9HxBMtsKvnsfPDvg9muOjjn"

# TODO - by updating the assistant it turned off file search, you need to update it with all the tools you want to use
print(add_tool_to_assistant(client, assisant_id))