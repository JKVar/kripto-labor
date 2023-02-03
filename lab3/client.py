# this is the client
import sys
import socket
import merkle_hellman as mh

host = '0.0.0.0'
server_port = 9000
help_msg = '''
python client.py [port]
[port] - a number bigger than 1024
    ex: python client.py 9001
'''


def regist_to_keyserver(my_name, public_key):
    ssocket = socket.socket()
    ssocket.connect((host, server_port))
    req = 'HENLO'
    ssocket.send(req.encode())
    recv_msg = ssocket.recv(1024).decode()

    if recv_msg == 'HENLO':
        msg = 'MY_NAME_IS ' + str(my_name)
        ssocket.send(msg.encode())
        recv_msg = ssocket.recv(1024).decode()

        if recv_msg == 'WHAT ' + my_name:
            transformed_key = str(public_key).strip('()')
            ssocket.send(transformed_key.encode())
            recv_msg = ssocket.recv(1024).decode()
            ssocket.close()

            return recv_msg == 'OK'
    
    ssocket.close()
    return False

def find_user_on_server(other_user):
    ssocket = socket.socket()
    ssocket.connect((host, server_port))
    req = 'HENLO'
    print(req)
    ssocket.send(req.encode())
    recv_msg = ssocket.recv(1024).decode()

    if recv_msg == 'HENLO':
        msg = 'FIND ' + str(other_user)
        ssocket.send(msg.encode())
        recv_msg = ssocket.recv(1024).decode()
        recv_msg = recv_msg.split()
        print('>>>>', recv_msg)

        if recv_msg[0] == 'PWD':
            public_key = tuple(map(lambda x: int(x.strip(',')),
                                recv_msg[1:len(recv_msg)-1]))
            print(public_key)
            ssocket.close()

            return public_key
    
    ssocket.close()
    return None

def begin_communication(other_user, opublic_key, private_key):
    print('> ')

def run_client(port):
    # generating public and provate keys
    public_key, private_key = mh.keygen_merkle_hellman()
    registered = regist_to_keyserver(port, public_key)
    
    if not registered:
        print('> registration failed')
        return 

    print('> successfull registration')

    other_user = input('Who do you want to talk to?\n>>> ')
    
    key = find_user_on_server(other_user)

    if not key:
        print('> not found other user')
        return 
    
    print('> found other user')

# checking the arguments
if len(sys.argv) == 1:
    print('port number missing')
    print(help_msg)
elif len(sys.argv) > 2:
    print('there must be only one argument')
    print(help_msg)
elif int(sys.argv[1]) <= 1024:
    print('the port number must be bigger than 1024')
    print(help_msg)
elif int(sys.argv[1]) == server_port:
    print(server_port, 'is the server\'s port')
else:
    run_client(sys.argv[1]) # stsrting client
