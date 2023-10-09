import socket

# Create a socket for communication with the master server (TCP)
node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('master', 6000)  # Replace with the actual IP address of the master server

try:
    # Connect to the master server (TCP)
    node_socket.connect(master_address)

    # Receive a message from the master (TCP)
    data = node_socket.recv(1024).decode()
    print(f"Received message from the master: {data}")

finally:
    # Close the connection with the master (TCP)
    node_socket.close()


# Create a socket for listening to multicast messages
multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
multicast_group = '224.1.1.1'
multicast_port = 6002

# Bind the multicast socket to the multicast group and port
multicast_socket.bind(('0.0.0.0', multicast_port))

# Join the multicast group
multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                            socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

while True:

    # Receive multicast messages
    multicast_data, _ = multicast_socket.recvfrom(1024)
    print(f"Received multicast message: {multicast_data.decode()}")
