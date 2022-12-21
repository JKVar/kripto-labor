# this is the keyserver
import socket
import threading

lock = threading.Lock()

host = '0.0.0.0'
server_port = 8000
s = socket.socket()
s.bind((host, server_port))
s.listen(1)

def register_user(client, user_name, user_list):
    print('> registering user', user_name)
    msg = 'WHAT ' + user_name
    client.send(msg.encode())

    pwd = client.recv(1024).decode()
    lock.acquire()
    user_list[user_name] = pwd
    lock.release()
    print('> saving', user_name + ',s public key')

    ok_msg = 'OK'
    client.send(ok_msg.encode())

def find_user(client, user_name, user_list):
    print('> searching user', user_name)

    if user_name not in user_list:
        msg = 'NOT ' + user_name
        client.send(msg.encode())
        print('>', user_name, 'not found')
        return

    lock.acquire()
    public_key = 'PWD ' + user_list[user_name]
    lock.release()
    client.send(public_key.encode())
    print('> user ', user_name, 'is found')

def talk_with_client(client, user_list):
    print('> talking with client')
    msg = 'HENLO'.encode()
    client.send(msg)

    recv_msg = client.recv(1024).decode()
    req = recv_msg.split()

    if req[0] == 'MY_NAME_IS':
        what = req[1]
        register_user(client, what, user_list)
        print('> registration done for ', what)
    elif req[0] == 'FIND':
        what = req[1]
        find_user(client, what, user_list)
        print('>', what, 'found')

user_list = {}
while True:
    client, client_addr = s.accept()
    recv_msg = client.recv(1024)

    if recv_msg == 'stop':
        break

    th = threading.Thread(target=talk_with_client, 
                args=(client, user_list, ))

    # th.daemon = True
    th.start()

s.close()
