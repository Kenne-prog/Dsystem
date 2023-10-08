import socket

master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('0.0.0.0', 6000)

master_socket.bind(master_address)
master_socket.listen(4)

connected_nodes = []

try:
    while True:
        node_socket, node_address = master_socket.accept()
        connected_nodes.append((node_socket, node_address))

        while True:
            message = node_socket.recv(1024).decode()  # Receive messages from nodes

            if not message:
                break  # Connection closed by the node

            # Implement message handling logic here
            # Example: Check message type (e.g., BROADCAST, ANYCAST) and process accordingly
            if message.startswith('BROADCAST'):
                broadcast_message = message.split(':')[1]
                # Handle the broadcast message
                # Send response if needed
            elif message.startswith('ANYCAST'):
                anycast_message = message.split(':')[1]
                # Implement anycast logic to determine the nearest node and send the message

except KeyboardInterrupt:
    pass

finally:
    for node_sock, _ in connected_nodes:
        node_sock.close()
    master_socket.close()
