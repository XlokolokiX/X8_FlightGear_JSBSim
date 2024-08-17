import socket
import math

class Instruments:
    def __init__(self, address, listener_port):
        self.__address = address
        self.__listener_port = listener_port
        self.position:float = [0.0,0.0,0.0]
        self.angles:float = [0.0,0.0,0.0]
        self.rates:float = [0.0,0.0,0.0]
        self.track:float = 0.0
        self.airspeed:float = 0.0
        self.groundspeed:float = 0.0

    def __UpdateInstrumentData(self):
        try:
            
            listener_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            listener_socket.bind((self.__address, self.__listener_port))
            data, addr = listener_socket.recvfrom(300)
            listener_socket.close()

            data = data.decode('utf-8').removesuffix('\n').split('\t')
            data = [float(num) for num in data]
            self.position[0] = data[0]      #latitude-deg
            self.position[1] = data[1]      #longitude-deg
            self.position[2] = data[2]      #altitude-ft
            self.track = data[3]            #track-deg
            self.angles[0] = data[4]        #pith-deg
            self.angles[1] = data[5]        #roll-deg
            self.angles[2] = data[6]        #yaw-deg
            self.rates[0] = data[7]         #pith-rate-deg_s
            self.rates[1] = data[8]         #roll-rate-deg_s
            self.rates[2] = data[9]         #yaw-rate-deg_s
            self.airspeed = data[10]        #airspeed-kt
            self.groundspeed = data[11]     #groundspeed-kt

        except socket.error as e:
            print(f'Error receiving data: {e}')
            return None
        return data
    
    def get_position(self):
        self.__UpdateInstrumentData()
        return self.position
    def get_angles(self):
        self.__UpdateInstrumentData()
        return self.angles
    def get_rates(self):
        self.__UpdateInstrumentData()
        return self.rates
    def get_track(self):
        self.__UpdateInstrumentData()
        return self.track
    def get_airspeed(self):
        self.__UpdateInstrumentData()
        return self.airspeed
    def get_groundspeed(self):
        self.__UpdateInstrumentData()
        return self.groundspeed
