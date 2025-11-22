import socket

# HOST = "127.0.0.1" # Alamat IP lokal
HOST = "10.255.255.1"  # Alamat IP yang tidak dapat dijangkau
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Timeout 3 detik saat connect
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Berhasil connect!")

    # Timeout 2 detik saat read
    client.settimeout(2)
    data = client.recv(1024).decode()
    print("Data diterima:", data)

except socket.timeout:
    print("Koneksi timeout!")
finally:
    client.close()
