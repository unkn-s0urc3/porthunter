import socket
from colorama import Fore, Style, init

# Initialize colorama for color support
def scan_ports(host, start_port, end_port):
    open_ports = []

    # Loop through the range of ports
    for port in range(start_port, end_port + 1):
        print(Fore.GREEN + f"Scanning port {port}..." + Style.RESET_ALL)  # Print the message for the current port being checked

        # Create a socket for connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set the timeout for the connection

        result = sock.connect_ex((host, port))  # Try to connect
        if result == 0:
            open_ports.append(port)  # Port is open
        sock.close()  # Close the connection

    return open_ports


# Function to display ASCII art
def print_ascii_art():
    print(Fore.LIGHTGREEN_EX + "|------------------------------------------------------------------------------------------------------|")
    print("|*  ##  ##   ##  ##   ##  ##   ##  ##             ####     ####    ##  ##    ####    #####     ####   *|")
    print("|*  ##  ##   ### ##   ## ##    ### ##            ##  ##   ##  ##   ##  ##   ##  ##   ##  ##   ##  ##  *|")
    print("|*  ##  ##   ######   ####     ######            ##       ##  ##   ##  ##   ##  ##   ##           ##  *|")
    print("|*  ##  ##   ######   ###      ######   ######    ####    ##  ##   ##  ##   #####    ##         ###   *|")
    print("|*  ##  ##   ## ###   ####     ## ###                ##   ##  ##   ##  ##   ####     ##           ##  *|")
    print("|*  ##  ##   ##  ##   ## ##    ##  ##            ##  ##   ##  ##   ##  ##   ## ##    ##  ##   ##  ##  *|")
    print("|*   ####    ##  ##   ##  ##   ##  ##             ####     ####     ####    ##  ##    ####     ####   *|")
    print("|------------------------------------------------------------------------------------------------------|")
    print("|Author: unkn-s0urc3                                                                                   |")
    print("|Project: porthunter                                                                                   |")
    print("|Description: Scans a range of ports on a given host (IP address or domain name)                       |")
    print("|to check which ports are open                                                                         |")
    print("|------------------------------------------------------------------------------------------------------|\n" + Style.RESET_ALL)

if __name__ == "__main__":
    print_ascii_art()
    host = input(Fore.GREEN + "Enter the IP address or domain name: " + Style.RESET_ALL)
    try:
        start_port = int(input(Fore.GREEN + "Enter the starting port: " + Style.RESET_ALL))
        end_port = int(input(Fore.GREEN + "Enter the ending port: " + Style.RESET_ALL))

        if start_port < 0 or end_port < 0 or start_port > end_port:
            print(Fore.RED + "Error: Invalid port range. Please enter valid port numbers." + Style.RESET_ALL)
        else:
            open_ports = scan_ports(host, start_port, end_port)

            if open_ports:
                print(Fore.GREEN + f"Open ports: {open_ports}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No open ports found in the specified range." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Please enter valid numeric values for ports." + Style.RESET_ALL)