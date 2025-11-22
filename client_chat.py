import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print("Pesan masuk:", msg)
        except:
            break

def send():
    while True:
        message = input("")
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
