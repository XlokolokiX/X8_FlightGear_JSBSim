Los protocolos deben ser colocados en la carpeta FG/Data/Protocol

Iniciar FG con los siguientes argumentos en config: 'fgfs  --max-fps=50 --fov=110 --units-meters --httpd=8000 --generic=socket,out,50,localhost,5500,udp,sensors_protocol --generic=socket,in,50,,5501,udp,inputs_protocol'

Iniciar FG con https://sourceforge.net/p/flightgear/fgaddon/HEAD/tree/trunk/Aircraft/ATI-Resolution/

En http://localhost:8080 Se tiene una interfaz de usuario para visualizar el mapa en tiempo real e atributos