from aircraft import Plane
from autopilot import Autopilot
import time

X8 = Plane('localhost', 5500, 5501)
auto1 = Autopilot(X8)
X8.setThrottle(1)
try:
    while True:
        elevator = auto1.altitude_hold(500)
        print(elevator)
        time.sleep(20e-3)

except KeyboardInterrupt as e:
    del(X8)
    del(auto1)
    print('Exiting ...')
    