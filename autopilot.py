import math
from simple_pid import PID
from instruments import Instruments
from aircraft import Plane

class Autopilot:
    def __init__(self, plane:Plane) -> None:
        self.plane = plane
    
    def __saturation(self, value:float, low_limit:float, high_limit:float):
        if(value < low_limit):
            return low_limit
        if(value > high_limit):
            return high_limit
        return value 

    def altitude_hold(self, altitude:float):
        '''
        Mantains a demanded altitude using PITCH attitude
        :param altitude: Desired altitude [feet]
        :return: None
        '''
        kp = 0.0005
        ki = 0.025
        kd = 0
        error = altitude - self.plane.instruments.getGPSaltitude()

        altitude_controller = PID(kp, ki, kd)
        output = altitude_controller(error)
        output = self.__saturation(output, low_limit = -10*(math.pi/180), high_limit = 10*(math.pi/180))#Prevent excesive Pitch
        self.plane.setElevator(output)
        self.heading_hold(180)
        return output
    
    def heading_hold(self, heading:float):
        '''
        Mantains a demanded heading using magnetic heading using Roll Attitude
        :param heading: Desired heading [degree]
        :return: None
        '''
        kp = 0.001
        ki = 0.08
        kd = 0.05
        error = heading - self.plane.instruments.getmagneticHeading()
        heading_controller = PID(kp, ki, kd)
        output = heading_controller(-error)
        output = self.__saturation(output, low_limit = -3*(math.pi/180), high_limit = 3*(math.pi/180))#Prevent excesive Roll
        self.plane.setAilerons(output)
        return output

    def pitch_hold(self, pitch:float):
        '''
        Mantains a commanded pitch attitude using PI controller with a rate component
        :param pitch: Desired pitch attitude [radians]
        :return: None
        '''

        kp = 1
        ki = 0
        kd = 0.03
        error = pitch - self.instruments.getAttitude()[0]
        controller = PID(kp, ki, 0.0)
        output = controller(error)