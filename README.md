
# Distributed Query Processing in Distributed Database Systems

## Project Overview

This project implements a distributed query processing system across multiple nodes, where queries are distributed to different nodes in the network, processed in parallel, and results are aggregated and returned to the client. The system simulates a distributed database environment using SQLite, with nodes running on different ports and querying a shared database.

## Features

- **Distributed Query Processing**: Queries are sent to different nodes for processing.
- **Parallel Query Execution**: Multiple nodes handle different parts of the query.
- **Simple Database**: The project uses SQLite to simulate a distributed database system.
- **Testing**: Includes a test file to ensure the functionality of the system.

## Prerequisites

- Python 3.x
- SQLite (comes with Python)
- Basic knowledge of how socket programming works

## File Structure

```
DistributedDB_Project/
│
├── node_server.py          # The main node server file that handles incoming queries
├── central_client.py       # The client that sends queries to multiple nodes
├── setup_node_database.py  # Sets up the initial database with sample data
├── test_node_server.py     # Tests the functionality of the node server
├── config.json             # Configuration file for setting node host and port
└── README.md               # This file
```

## Setup Instructions

### 1. Set Up the Database

Before running the project, you need to set up the initial database. Run the following command to initialize the database and insert sample data:

```bash
python setup_node_database.py
```

This will create the database `node_database.db` and populate it with the sample data.

### 2. Start Node Servers

Each node server runs on a different port. To simulate a distributed environment, you need to run multiple instances of the `node_server.py` file on different ports.

For example, run the following commands in separate terminal windows:

```bash
python node_server.py
```

In the `config.json` file, change the **port number** for each instance of `node_server.py`. You can set `port` to different values (e.g., `5001`, `5002`, `5003`) for each instance.

### 3. Run the Central Client

The central client sends queries to the nodes and aggregates the results. To run the client and interact with the system:

```bash
python central_client.py
```

Enter your SQL queries in the prompt, and the system will distribute the query to the nodes, process it, and return the results.

### 4. Running Tests

To test the functionality of the node server and ensure it is working correctly, run the test file:

```bash
python test_node_server.py
```

This will simulate queries and check if the server responds correctly.

## Example Queries

You can test with the following SQL queries:

1. **Get all employees**:
   ```sql
   SELECT * FROM Employees;
   ```

2. **Get employees in Engineering department**:
   ```sql
   SELECT * FROM Employees WHERE department = 'Engineering';
   ```

3. **Get employees in NY**:
   ```sql
   SELECT * FROM Employees WHERE location = 'NY';
   ```

## How It Works

1. **Client**: The central client sends SQL queries to multiple nodes (servers).
2. **Nodes**: Each node processes the query and returns the result to the client.
3. **Query Processing**: The query results are aggregated and returned to the client in parallel.

## Troubleshooting

- **Error: `WinError 10048`** (Address already in use): This means that the port you're trying to bind to is already occupied. Try changing the port number in the `config.json` file and restarting the node server.
  
- **Issue with Database Setup**: If the database isn't set up properly, ensure that `setup_node_database.py` has been run successfully before starting the node servers.

## Conclusion

This project demonstrates the basic concept of query processing in a **distributed database system**. The system processes queries across multiple nodes in parallel, simulating a distributed environment, and it is tested for functionality using a simple test suite.

