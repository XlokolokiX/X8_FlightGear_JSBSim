from aircraft import Plane
from autopilot import Autopilot
import time

X8 = Plane('localhost', 5500, 5501)
X8.setWeather(0)
auto1 = Autopilot(X8)
X8.setThrottle(0.5)
contador = 100
try:
    while(True):
        auto1.altitude_hold(500)
        
        contador -= contador

        if(contador == 0):
            print(X8.elevator)
            print(X8.instruments.get_position()[2])
            contador = 100
        time.sleep(20e-3)

except KeyboardInterrupt as e:
    del(auto1)
    del(X8)
    print("Exiting")