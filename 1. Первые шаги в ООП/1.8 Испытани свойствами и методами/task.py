class Data:
    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip


class Server:
    _count = 0

    def __init__(self) -> None:
        __class__._count += 1
        self.buffer = []
        self.ip = __class__._count
        self.router = None

    def send_data(self, data):
        '''для отправки информационного пакета data (объекта класса Data)
         с указанным IP-адресом получателя (пакет отправляется роутеру и
         сохраняется в его буфере - локальном свойстве buffer);'''
        if self in self.router._connect:
            self.router.buffer.append(data)
        else:
            print('Сервер не подключен к роутеру')

    def get_data(self):
        '''возвращает список принятых пакетов (если ничего принято не было,
         то возвращается пустой список) и очищает входной буфер;'''
        swap = self.buffer.copy()
        self.buffer.clear()
        return swap

    def get_ip(self):
        '''возвращает свой IP-адрес.'''
        return self.ip


class Router:
    def __init__(self) -> None:
        self._connect = []
        self.buffer = []

    def link(self, server):
        '''для присоединения сервера server (объекта класса Server) к роутеру
         (для простоты, каждый сервер соединен только с одним роутером);'''
        self._connect.append(server)
        server.router = self

    def unlink(self, server):
        ''' для отсоединения сервера server (объекта класса Server)
         от роутера;'''
        self._connect.remove(server)

    def send_data(self):
        '''для отправки всех пакетов (объектов класса Data) из буфера роутера
         соответствующим серверам (после отправки буфер должен очищаться).'''
        for serv in self._connect:
            for d in self.buffer:
                if serv.ip == d.ip:
                    serv.buffer.append(d)
        self.buffer.clear()


# Тесты
if __name__ == "__main__":

    assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(
        Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
    assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(
        Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

    router = Router()
    sv_from = Server()
    sv_from2 = Server()
    router.link(sv_from)
    router.link(sv_from2)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    sv_from2.send_data(Data("Hello", sv_to.get_ip()))
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()

    assert len(
        router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
    assert len(
        sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

    assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

    assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

    assert hasattr(router, 'buffer') and hasattr(
        sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

    router.unlink(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    router.send_data()
    msg_lst_to = sv_to.get_data()
    assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
