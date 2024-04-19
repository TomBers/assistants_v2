from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

assisant_id = "asst_N9HxBMtsKvnsfPDvg9muOjjn"

client = OpenAI()

assistant = client.beta.assistants.retrieve(assisant_id)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I would like to know what kWh means."
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
  print(messages)
else:
  print(run.status)