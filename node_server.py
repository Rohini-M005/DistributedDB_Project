import socket
import sqlite3
import json

# Load config from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Function to execute SQL query on the node database
def execute_query(query):
    conn = sqlite3.connect(config["db_name"])  # Connect to the node database
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return str(result)

# Function to run the node server
def node_server():
    host = config["node_host"]
    for port in config["node_ports"]:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            server_socket.listen(5)
            print(f"Node server started at {host}:{port}")

            while True:
                client_socket, _ = server_socket.accept()
                query = client_socket.recv(1024).decode()
                print(f"Received query: {query}")
                result = execute_query(query)
                client_socket.send(result.encode())
                client_socket.close()

        except OSError as e:
            print(f"Error with port {port}: {e}")

if __name__ == "__main__":
    node_server()
