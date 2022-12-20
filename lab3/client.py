# this is the client
import sys

server_port = 9000
help_msg = '''
python client.py [port]
[port] - a number bigger than 1024
    ex: python client.py 9001
'''

def run_client(port):
    print('client_id: ', port)
    print('server port: ', server_port)

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
