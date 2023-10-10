import socket
import time
import csv

communication = 'Communication.csv'
def main():
    
    # Create a set to store received multicast messages
    received_messages = set()

    # Create a socket for communication with the master server (TCP)
    node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_address = ('master', 6000)  # Replace with the actual IP address of the master server

    try:
        # Connect to the master server (TCP)
        node_socket.connect(master_address)

        # Receive a message from the master (TCP)
        data = node_socket.recv(1024).decode()
        print(f"Received message from the master: {data}")
        log_communication("Broadcast", socket.gethostbyname('master'), 6000, socket.gethostbyname(socket.gethostname()), 6000, len(data))

    finally:
        # Close the connection with the master (TCP)
        node_socket.close()

    # Create a socket for listening to multicast messages
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_group = '224.1.1.1'
    multicast_port = 6006

    # Bind the multicast socket to the multicast group and port
    multicast_socket.bind(('0.0.0.0', multicast_port))

    # Join the multicast group
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                                socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

    while True:
        # Receive multicast messages
        multicast_data, _ = multicast_socket.recvfrom(1024)
        message = multicast_data.decode()

        # Check if the message has already been received to deduplicate
        if message not in received_messages:
            received_messages.add(message)
            print(f"Received multicast message: {message}")
            log_communication("Multicast", '0.0.0.0', multicast_port, multicast_group, multicast_port, len(message))

def log_communication(protocol, source_ip, source_port, destination_ip, destination_port, length):
    current_time = time.time()
    log_entry = [protocol, current_time, source_ip, destination_ip, source_port, destination_port, length]

    with open(communication, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(log_entry)
if __name__=='__main__':
    main()