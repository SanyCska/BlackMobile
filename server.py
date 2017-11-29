from socket import *
HOST = 'localhost'  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 21112  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 1024  # размер буфера 1Кбайт
ADDR = (HOST, PORT)  # адрес сервера
tcpSerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
tcpSerSock.bind(ADDR)  # связываем сокет с адресом
tcpSerSock.listen(5)  # устанавливаем максимальное число клиентов одновременно обслуживаемых
while True:  # бесконечный цикл сервера
    print('Waiting for client...')

    tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет tcpCliSock)

    print('Connected from: {}'.format(addr))

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        data.decode('utf8')
        if data:
            print(data)

tcpSerSock.close()  # закрытие сокета сервера