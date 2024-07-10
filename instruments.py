import socket
import math

class Instruments:
    def __init__(self, listener_socket:socket):
        self.listener_socket = listener_socket
        self.gps:float = [0.0,0.0]
        self.gpsAltitude:float = 0.0
        self.altitude:float = 0.0
        self.attitude:float = [0.0,0.0]
        self.magneticHeading:float = 0.0

    def __UpdateInstrumentData(self):
        data, addr = self.listener_socket.recvfrom(2048)
        data = data.decode('utf-8').removesuffix('\n').split('\t')
        data = [float(num) for num in data]
        self.gps[0] = data[0]       #latitude
        self.gps[1] = data[1]       #longitude
        self.gpsAltitude = data[2]       #altitude gps (M)
        self.altitude = data[3]     #altitude sensor
        self.attitude[0] = data[4]  #Pitch
        self.attitude[1] = data[5]  #Roll
        self.magneticHeading = data[6] #Heading
        return data
    
    def __radians_to_mercator(self, lat_rad, lon_rad, radius=6371000):
        x = radius * lon_rad
        y = radius * math.log(math.tan(math.pi / 4 + lat_rad / 2))
        return [x, y]

    def getGPSradians(self):
        self.__UpdateInstrumentData()
        return self.gps
    
    def getGPScoordinates(self):
        gps = self.getGPSradians()
        return self.__radians_to_mercator(gps[0], gps[1])
    
    def getGPSaltitude(self):
        self.__UpdateInstrumentData()
        return self.gpsAltitude
    
    def getAttitude(self):
        self.__UpdateInstrumentData()
        return self.attitude
    
    def getmagneticHeading(self):
        self.__UpdateInstrumentData()
        return self.magneticHeading