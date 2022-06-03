import message as ms
import socket

HOST = "10.176.93.182"
PORT = 5005


if __name__ == '__main__':
    #This code sends a text message to our endangered user
    #ms.send('+972504874011', 'זוהתה הצפה בקרבת ביתך, אנא עלה\י אל מקום גבוה')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if data == b"exit":
                    break
                elif data == b"morb":
                    print("IT'S MORBIN TIME")
                elif data == b"Flood":
                    ms.send('+972504874011', 'זוהתה הצפה דרך חיישן 1')
                    break
                else:
                    ms.send('+972504874011', 'זוהתה הצפה דרך חיישן 1')
                conn.sendall(data)


