import socket

# Function to scan ports
def scan_ports(host, start_port, end_port):
    open_ports = []

    # Loop through the range of ports
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")  # Print the message for the current port being checked

        # Create a socket for connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set the timeout for the connection

        result = sock.connect_ex((host, port))  # Try to connect
        if result == 0:
            open_ports.append(port)  # Port is open
        sock.close()  # Close the connection

    return open_ports

if __name__ == "__main__":
    host = input("Enter the IP address or domain name: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found in the specified range.")
