# Simple HTTP Server
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Define the handler to serve files from the current directory
class SimpleEndpoint(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        query_params = parse_qs(parsed_path.query)
        print(query_params)
        
        response_data = [
        {
            "name": "Tariff 1",
            "price": 500
        },
        {
            "name": "Tariff 2",
            "price": 1200
        },
        {
            "name": "Tariff 3",
            "price": 2300
        },
         {
            "name": "Tariff 4",
            "price": 700
        }
    ]
        json_response = json.dumps(response_data)
        # Respond with a simple text message
        self.send_response(200)  # Send OK status
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_response.encode())


# Set the server address and port
server_address = ('', 8001)

# Create an HTTP server instance
httpd = HTTPServer(server_address, SimpleEndpoint)

# Start the server
print("Serving at port 8001")
httpd.serve_forever()