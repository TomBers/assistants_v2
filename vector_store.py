def retrieve_vector_store(client):
    vec_store_id = "vs_2wLBjnmpVKbcZMR3gPtyVy8y"
    return client.beta.vector_stores.retrieve(vector_store_id=vec_store_id)

def add_file_to_vector_store(client, vector_store, file):
    return client.beta.vector_stores.files.create(vector_store_id=vector_store.id, file_id=file.id)

def clean_up_files(client, vector_store, files):
    for f in files:
        client.beta.vector_stores.files.delete(vector_store_id=vector_store.id, file_id=f.id)
        client.files.delete(file_id=f.id)

def file_upload(client, file):
    return client.files.create(file=open(file.path, "rb"), purpose="assistants")