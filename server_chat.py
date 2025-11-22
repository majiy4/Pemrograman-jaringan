import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"Client terhubung: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"{addr}: {msg.decode()}")
            broadcast(msg, conn)
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"Client terputus: {addr}")

print("Chat Server berjalan...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
