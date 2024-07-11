from aircraft import Plane
from autopilot import Autopilot
import time

Malolo1 = Plane('localhost', 5500, 5501)
auto1 = Autopilot(Malolo1)
Malolo1.setThrottle(1)
try:
    while True:
        elevator = auto1.altitude_hold(300)
        print(elevator)
        time.sleep(20e-3)

except KeyboardInterrupt as e:
    del(Malolo1)
    del(auto1)
    print('Exiting ...')
