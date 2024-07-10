import socket
from instruments import Instruments

class Plane:
    def __init__(self, Address:str = 'localhost', listener_Port:int = 5500, writing_Port:int = 5501):
        self.__Address = Address
        self.__listener_Port = listener_Port
        self.__writing_Port = writing_Port
        self.writing_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        listener_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        listener_socket.bind((self.__Address, self.__listener_Port))
        self.instruments = Instruments(listener_socket=listener_socket)

        self.ailerons = 0.0
        self.elevator = 0.0
        self.throttle = 0.0

    def __updatePLane(self):
        data = f'{self.ailerons},{self.elevator},{self.throttle}\n'
        self.writing_socket.sendto(data.encode('utf-8'), (self.__Address, self.__writing_Port))

    def setAilerons(self, value:float = 0.0):
        self.ailerons = value
        self.__updatePLane()
    def setElevator(self, value:float = 0.0):
        self.elevator = value
        self.__updatePLane()
    def setThrottle(self, value:float = 0.0):
        self.throttle = value
        self.__updatePLane()
        
