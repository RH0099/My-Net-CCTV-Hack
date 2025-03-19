import os
import time
import nmap
from termcolor import colored

# Function for displaying the intro message
def show_intro():
    print(colored("================================================", "blue"))
    print(colored("   Welcome to the CCTV Camera and Network Tool", "green"))
    print(colored("================================================", "blue"))
    print("\n1. Scan Network")
    print("2. Admin Panel Finder and Brute Force")
    print("3. Exit\n")

# Function to scan network and find devices
def scan_network():
    ip_range = input("Enter the IP range to scan (e.g. 192.168.1.0/24): ")
    nm = nmap.PortScanner()
    print(colored("\nScanning network, please wait...", "yellow"))
    nm.scan(hosts=ip_range, arguments='-sn')  # -sn for Ping Scan
    print(colored("\nScan complete. Devices found:", "green"))

    for host in nm.all_hosts():
        print(f"IP Address: {host}, Hostname: {nm[host].hostname()}")
        if 'tcp' in nm[host]:
            print(f"Open Ports: {nm[host]['tcp']}")
        if "osmatch" in nm[host]:
            print(f"Device Type: {nm[host]['osmatch']}")
        print("-" * 50)

# Function to find Admin Panel and apply Brute Force (mockup for now)
def admin_panel_brute_force():
    print(colored("\nSearching for Admin Panel and applying Brute Force...", "yellow"))
    # This is a placeholder for the Brute Force functionality.
    # Replace with actual Brute Force logic based on the Admin Panel URL
    print(colored("\nAdmin Panel found at: 192.168.1.10", "green"))
    print(colored("Attempting Brute Force Attack... (this is a mockup)", "red"))
    time.sleep(2)
    print(colored("Brute Force Complete: Password cracked successfully", "green"))
    print("Username: admin, Password: admin123")

# Function to view live CCTV stream (mockup for now)
def view_cctv_stream():
    print(colored("\nAttempting to view CCTV live stream...", "yellow"))
    # Replace with actual live stream logic (e.g., RTSP stream or camera URL)
    print(colored("Live Stream displayed in default media player...", "green"))
    os.system("ffplay rtsp://192.168.1.100:554/stream")  # Sample RTSP URL

# Main function to control the flow
def main():
    while True:
        show_intro()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            scan_network()
        elif choice == '2':
            admin_panel_brute_force()
        elif choice == '3':
            print(colored("\nExiting the tool. Goodbye!", "blue"))
            break
        else:
            print(colored("\nInvalid choice, please try again.", "red"))

# Run the main function
if __name__ == "__main__":
    main()
