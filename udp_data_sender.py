import socket
import time

relay_host = "45.135.233.152"
relay_port = 11373

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_data_to_relay(message):
    global relay_host, relay_port, sender_socket
    
    sender_socket.sendto(message.encode(), (relay_host, relay_port))
    print(f"Sent message to relay: {message}")
    

if __name__ == "__main__":
    

    # Отправка тестового сообщения
    send_data_to_relay("Hello from Sender!")

    # Отправка текущего времени в цикле с периодом в 1 секунду
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        send_data_to_relay(f"Current time: {current_time}")
        time.sleep(1)
