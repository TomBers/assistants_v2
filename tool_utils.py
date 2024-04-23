import json

def extract_parameter_names(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            parameters = data.get('parameters', {}).get('properties', {})
            parameter_names = list(parameters.keys())
        return parameter_names