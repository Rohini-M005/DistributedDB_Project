import socket
import json
import ast

# Load config from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Function to send a query to a node
def send_query_to_node(host, port, query):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(query.encode())
        result = client_socket.recv(1024).decode()
        return result

# Function to send query to all nodes in parallel and aggregate results
def parallel_query(query):
    nodes = config["node_ports"]  # List of node ports
    results = []

    for port in nodes:
        host = config["node_host"]
        print(f"Attempting to connect to node at {host}:{port}...")
        result = send_query_to_node(host, port, query)
        print(f"Received result from node at {host}:{port}")
        results.append(result)

    return aggregate_results(results)

# Function to aggregate results from all nodes
def aggregate_results(results):
    final_result = []
    for result in results:
        try:
            final_result.extend(ast.literal_eval(result))  # Converting string back to list format
        except Exception as e:
            print(f"Error evaluating result: {e}")
    return final_result

# Main function to handle user input and send queries
if __name__ == "__main__":
    while True:
        query = input("Enter SQL query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        print("Attempting to connect to nodes...")
        result = parallel_query(query)
        print("Query Result:", result)
