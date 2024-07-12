import socket
from instruments import Instruments

class Plane:
    def __init__(self, Address:str = 'localhost', listener_Port:int = 5500, writing_Port:int = 5501):
        self.ailerons = 0.0
        self.elevator = 0.0
        self.throttle = 0.0
        self.__Address = Address
        self.__writing_Port = writing_Port

        try:
            self.writing_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.instruments = Instruments(address = Address, listener_port = listener_Port)
        except socket.error as e:
            print(f'Failed to create bind socket: {e}')
            raise

    def __updatePLane(self):
        data = f'{self.ailerons},{self.elevator},{self.throttle}\n'
        try:
            self.writing_socket.sendto(data.encode('utf-8'), (self.__Address, self.__writing_Port))
            return True
        except socket.error as e:
            print(f'Error sending control data: {e}')
            return False

    def setAilerons(self, value:float = 0.0):
        self.ailerons = value
        self.__updatePLane()
    def setElevator(self, value:float = 0.0):
        self.elevator = value
        self.__updatePLane()
    def setThrottle(self, value:float = 0.0):
        self.throttle = value
        self.__updatePLane()
    def getInstruments(self):
        return self.instruments

    def __del__(self):
        self.setAilerons(0)
        self.setElevator(0)
        self.setThrottle(0)
        try:
            self.writing_socket.close()
        except socket.error as e:
            print(f'Error closing Writing Socket: {e}')
        
        