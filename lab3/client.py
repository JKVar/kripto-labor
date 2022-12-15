# this is the client
import sys

help_msg = '''
python client.py [port]
port - a number bigger than 1024
'''

def run_client(port):
    print('client_id: ', port)

if len(sys.argv) == 1:
    print('port number missing')
    print(help_msg)
elif len(sys.argv) > 2:
    print('there must be only one argument')
    print(help_msg)
elif int(sys.argv[1]) <= 1024:
    print('the port number must be bigger than 1024')
    print(help_msg)
else:
    run_client(sys.argv[1])
