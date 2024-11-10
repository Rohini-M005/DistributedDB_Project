import socket

def test_node_connection(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(b"SELECT * FROM Employees")
            response = s.recv(1024).decode()
            print(f"Response from server: {response}")
    except Exception as e:
        print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    host = "127.0.0.1"
    ports = [5001, 5002, 5003]
    for port in ports:
        print(f"Testing connection to node at {host}:{port}")
        test_node_connection(host, port)
