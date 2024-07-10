from aircraft import Plane

Malolo1 = Plane('localhost', 5500, 5501)

Malolo1.setElevator(-0.015)
Malolo1.setAilerons(0)
Malolo1.setThrottle(1)
print(Malolo1.instruments.getGPSradians())