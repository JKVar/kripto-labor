import socket

def kaptamUzenetet(s):
  kapottUzenet = s.recv(1024).decode()
  while kapottUzenet[0] == '[':
    nemKell = kapottUzenet.split(']')[1]
    if nemKell != ' >>>':
        print(kapottUzenet)
    kapottUzenet = s.recv(1024).decode()

def uzenetKuldes(s):
  sor = ''
  uzenet = ''
  while sor != '.':
    sor = input('>>> ')
    if sor == '' or sor=='\n':
        sor = '>>>'
    s.send(sor.encode())
    # uzenet += sor
    kaptamUzenetet(s)
  # s.send(uzenet.encode())

host = '0.0.0.0'
port = 2001
s = socket.socket()
s.connect((host, port))

megy = 'go'
s.send(megy.encode())
# csatlakozva van
kapottUzenet = s.recv(1024).decode()
uzenet = 'IAM '
myName = input('username: ')
uzenet += myName + '\n'
s.send(uzenet.encode())
kapottUzenet=s.recv(1024).decode().strip('\n')
while kapottUzenet == 'USER EXISTS':
  myName = input('username: ')
  uzenet += myName + '\n'
  s.send(uzenet.encode())
  kapottUzenet=s.recv(1024).decode().strip('\n')


# visszakoszon
kapottUzenet = s.recv(1024).decode()
while kapottUzenet[0] == '[':
  print(kapottUzenet)
  kapottUzenet = s.recv(1024).decode()
# print(kapottUzenet)

parancsok = ['chat', 'public', 'quit', 'list', 'help']
help = "\tParancsok:\n\
        chat \t- privat uzenet kuldese\n\
        public \t- publikus uzenet kuldese\n\
        list \t- bejelentkezett felhasznalok listaja\n\
        help \t- ezt az uzenetet irja ki\n\
        quit \t- kilepes a chat alkalmazasbol\n\
        .\t- uzenet iras vege\n"
while True:
    # parancs elkuldese
    parancs = input('command> ')
    if parancs not in parancsok:
        print('[!] nincs ilyen parancs!')
        print(help)
        continue

    if parancs == 'help':
        print(help,'\n')
        continue

    s.send(parancs.encode())

    if parancs == 'chat':
      # visszakapja az uzenetet
      kapottUzenet = s.recv(1024).decode()
      while kapottUzenet[0] == '[':
        print(kapottUzenet)
        kapottUzenet = s.recv(1024).decode()
      # print(kapottUzenet)

      wrongUser = True
      while wrongUser:
        kinek = input('kinek> ')
        kinek += ':' + myName
        s.send(kinek.encode())
        # s.send(myName.encode())
        kapottUzenet = s.recv(1024).decode()
        if kapottUzenet == 'WRONG USERNAME':
          print('[!] nincs ilyen felhasznalo!')
        else:
          wrongUser = False

      while kapottUzenet[0] == '[':
        print(kapottUzenet)
        kapottUzenet = s.recv(1024).decode()
      # print(kapottUzenet)
      uzenetKuldes(s)
    elif parancs == 'public' :
      kapottUzenet = s.recv(1024).decode()
      while kapottUzenet[0] == '[':
        print(kapottUzenet)
        kapottUzenet = s.recv(1024).decode()
      print(kapottUzenet)

      s.send(myName.encode())
      kapottUzenet = s.recv(1024).decode()
      while kapottUzenet[0] == '[':
        print(kapottUzenet)
        kapottUzenet = s.recv(1024).decode()
      print(kapottUzenet)
      uzenetKuldes(s)
    elif parancs == 'quit':
      kapottUzenet = s.recv(1024).decode()
      s.send(myName.encode())
      kapottUzenet = s.recv(1024).decode()
      print(kapottUzenet)
      # print('kilepes sikeres')
      break
    elif parancs == 'list':
      users = s.recv(1024).decode()
      print(users,'\n')
    # elif parancs == 'stop':
    #   kapottUzenet = s.recv(1024).decode()
    #   if kapottUzenet == 'STOP':
    #     print(kapottUzenet)
    #     break
    #   else:
    #     print(kapottUzenet)
