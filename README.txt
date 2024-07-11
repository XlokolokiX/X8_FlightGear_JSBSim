1) Move ../FG_Protocol to FG/data/Protocol

2) Set FG with the following params. in configuration: 'fgfs  --max-fps=50 --fov=110 --units-meters --httpd=8000 --generic=socket,out,50,localhost,5500,udp,sensors_protocol --generic=socket,in,50,,5501,udp,inputs_protocol'

3) Start FG with https://sourceforge.net/p/flightgear/fgaddon/HEAD/tree/trunk/Aircraft/ATI-Resolution/ as Airplane

4) In http://localhost:8080 UI