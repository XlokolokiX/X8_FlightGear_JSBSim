from simple_pid import PID
import aircraft
import math
class Autopilot:

    def __init__(self, plane:aircraft):
        self.plane = plane
    
    def __saturation(self ,value:float ,lowLimit:float, highLimit:float):
        if (value < lowLimit): return lowLimit
        if (value > highLimit): return highLimit
        return value

    def altitude_hold(self, altitude:float):

        kp = 2
        ki = 5
        kd = 0

        error = altitude - self.plane.instruments.get_position()[2]
        altitude_controller = PID(kp, ki, kd)
        output = self.__saturation(altitude_controller(-error), lowLimit=-15*(math.pi/180) ,highLimit=20*(math.pi/180))
        self.pitch_hold(output)

    def pitch_hold(self, pitch:float):

        kp = 0.9
        ki = 0.0
        kd = 0.1

        error = pitch - self.plane.instruments.get_angles()[0]
        pitch_controller = PID(kp, ki, 0.0)
        pitch_rate_controller = PID(kd, 0.0, 0.0)
        output = pitch_controller(error)
        rate_output = pitch_rate_controller(self.plane.instruments.get_rates()[0])
        output = (output + rate_output)/30 #Normalización
        self.plane.setElevator(output)


        
