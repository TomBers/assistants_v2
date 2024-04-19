from openai import OpenAI
from tool import add_tool_to_assistant

client = OpenAI()

assisant_id = "asst_N9HxBMtsKvnsfPDvg9muOjjn"

print(add_tool_to_assistant(client, assisant_id))