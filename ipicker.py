import socket
import tkinter as tk

def extract_ip_and_port_from_url(url):
    protocol, rest = url.split("://")
    hostname = rest.split("/")[0].split(":")[0]
    port = 80
    if ":" in hostname:
        hostname, port = hostname.split(":")
        port = int(port)

    dest_ip = socket.gethostbyname(hostname)

    # Get the source IP address and port number using a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dest_ip, port))
    source_ip, source_port = s.getsockname()

    return protocol, source_ip, dest_ip, source_port, port

def show_results():
    url = entry.get()
    protocol, source_ip, dest_ip, source_port, dest_port = extract_ip_and_port_from_url(url)
    protocol_label.config(text=protocol)
    source_ip_label.config(text=source_ip)
    dest_ip_label.config(text=dest_ip)
    source_port_label.config(text=str(source_port))
    dest_port_label.config(text=str(dest_port))

root = tk.Tk()
root.title("IP and Port Extractor")

url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

extract_button = tk.Button(root, text="Extract", command=show_results)
extract_button.grid(row=0, column=2, padx=10, pady=10)

protocol_label = tk.Label(root, text="Protocol:")
protocol_label.grid(row=1, column=0, padx=10, pady=10)

source_ip_label = tk.Label(root, text="Source IP:")
source_ip_label.grid(row=2, column=0, padx=10, pady=10)

dest_ip_label = tk.Label(root, text="Destination IP:")
dest_ip_label.grid(row=3, column=0, padx=10, pady=10)

source_port_label = tk.Label(root, text="Source Port:")
source_port_label.grid(row=4, column=0, padx=10, pady=10)

dest_port_label = tk.Label(root, text="Destination Port:")
dest_port_label.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()
