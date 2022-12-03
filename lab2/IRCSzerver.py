import socket
import threading

lock = threading.Lock()

def sendTo(destination, uzenet):
    destination.send(uzenet.encode())

def parancsfeldolgozas(kliens, parancs, userList:dict):
    kilep = False
    uzenet = ''
    if parancs == 'chat':
        uzenet = '21 CHAT\n'
        kliens.send(uzenet.encode())

        wrongUser = True
        while wrongUser:
            uzenet = kliens.recv(1024).decode()
            nev = uzenet.split(':')[0]
            kitol = uzenet.split(':')[1]
            if nev not in userList:
                uzenet = 'WRONG USERNAME'
                kliens.send(uzenet.encode())
            else:
                wrongUser = False
        
        # kitol = kliens.recv(1024).decode()
        # kliens.send(' '.join(map(str,userList)))
        uzenet = '<' + kitol + '>'
        kliens.send(uzenet.encode())
        # uzenet = '[' + kitol + '] '
        uzenet = ''
        # print('uzi')
        # print(kliens)
        sor = ''
        while sor != '.':
            # sor = '[' + kitol + '] ' + kliens.recv(1024).decode()
            sor = kliens.recv(1024).decode()
            print(sor)
            kliens.send('> '.encode())
            # uzenet += '[' + kitol + '] ' + sor + '\n'
            uzenet = '[' + kitol + '] ' + sor + '\n'
            if nev in userList and sor != '.':
                sendTo(userList[nev], uzenet)
            # uzenet += sor
        
        # print(nev)
        # print(userList)
        # sendTo(userList[nev], uzenet)
    elif parancs == 'public' :
        uzenet = '21 CHAT\n'
        kliens.send(uzenet.encode())
        kitol = kliens.recv(1024).decode()

        uzenet = '<' + kitol + '>'
        kliens.send(uzenet.encode())
        uzenet = ''
        sor = ''
        while sor != '.':
            sor = kliens.recv(1024).decode()
            kliens.send('> '.encode())
            uzenet = '[' + kitol + '] ' + sor + '\n'
            for user in userList:
                if user != kitol and sor != '.':
                    sendTo(userList[user], uzenet)    

    elif parancs == 'quit':
        uzenet = 'EXIT REQUEST'
        kliens.send(uzenet.encode())
        nev = kliens.recv(1024).decode()
        userList.pop(nev)

        uzenet = 'QUIT'
        kliens.send(uzenet.encode())
        kilep = True
    elif parancs == 'list':
        users = ''
        for user in userList:
            users += user + ' '
        kliens.send(users.encode())
    # elif parancs == 'stop':
    #     if len(userList)<=1:
    #         uzenet = 'STOP'
    #         kilep = True
    #     else:
    #         uzenet = 'AWAKE'
    #     kliens.send(uzenet.encode())

    return kilep

def thFunction(kliens, userList:dict):
    # print(kliens)
    uzenet = '20 CONNECTED\n'
    kliens.send(uzenet.encode())

    kapottUzenet = kliens.recv(1024).decode()
    kliensNev = ''
    uzenet = '20 Hi '
    if kapottUzenet.split(' ')[0] == 'IAM':
        kliensNev = kapottUzenet.split(' ')[1].strip('\n')
        while kliensNev in userList:
            kliens.send('USER EXISTS'.encode())
            kliensNev = kapottUzenet.split(' ')[1].strip('\n')
        userList[kliensNev] = kliens
        uzenet += kliensNev
        kliens.send(uzenet.encode())
    else:
        kliens.send('40'.encode())
    
    kilepett = False
    while not kilepett:
        parancs = kliens.recv(1024).decode()
        kilepett = parancsfeldolgozas(kliens, parancs, userList)

    # print(parancs)
    # if parancs == 'stop':
    #     leall[0] = True
    #     kliens.close()

host = '0.0.0.0'
port = 2001
s = socket.socket()
s.bind((host, port))
s.listen(1)
# s.settimeout(100)

userList = {}
while True:
    kliens, kliensCim = s.accept()
    kapottUzenet = kliens.recv(1024).decode()
    if kapottUzenet == 'stop':
        print('> A szerver leall!\n')
        break
    print(kliensCim)
    th = threading.Thread(target=thFunction, args=(kliens,userList, ))
    th.daemon = True
    th.start()
    # print('kix')
    # th.join()

s.close()