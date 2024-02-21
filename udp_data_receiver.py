import socket
import time

relay_host = "45.135.233.152"
relay_port = 11373

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_data_to_relay(message):
    global relay_host, relay_port, receiver_socket
    
    receiver_socket.sendto(message.encode(), (relay_host, relay_port))
    print(f"Sent message to relay: {message}")
    
def receive_data_from_relay():
    while True:
        data, addr = receiver_socket.recvfrom(1024)  # Получаем данные
        print(f"Received message from {addr}: {data.decode()}")
        
        

if __name__ == "__main__":

    # Отправка тестового сообщения
    send_data_to_relay("Hello from Receiver!")
    
    receive_data_from_relay()
        

