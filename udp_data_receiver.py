import socket
import time
import struct

relay_host = "45.135.233.152"
relay_port = 11373

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_data_to_relay(message):
    global relay_host, relay_port, receiver_socket
    
    receiver_socket.sendto(message.encode(), (relay_host, relay_port))
    print(f"Sent message to relay: {message}")
    
def receive_data_from_relay():
    while True:
        data, addr = receiver_socket.recvfrom(256*4*4)  # Получаем данные
        print(f"Received message from {addr}: {data.size()} bytes")
        received_buffer = deserialize_float_array(data, 256, 4)
        
def deserialize_float_array(data, width, height):
    # Размер float в байтах: 4 байта (для формата 'f' в структуре)
    float_size = 4
    num_floats = width * height
    floats = struct.unpack(f'{num_floats}f', data)
    return [floats[i * width:(i + 1) * width] for i in range(height)]
        

if __name__ == "__main__":

    # Отправка тестового сообщения
    send_data_to_relay("Hello from Receiver!")
    
    receive_data_from_relay()
        

