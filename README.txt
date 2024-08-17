1) Move ../FG_Protocol to FG/data/Protocol

2) Set FG with the following params. in configuration: 'fgfs  --max-fps=50 --fov=90 --units-meters --httpd=8000 --generic=socket,out,50,localhost,5500,udp,sensors_protocol --generic=socket,in,50,,5501,udp,inputs_protocol'

3) Move AIRCRAFT Folder to FG/data/Aircraft

4) Inside FG Program, go to complements and add the AIRCRAFT Folder

5) Start FG with X8_FixedWing(R/C) as Airplane

6) In http://localhost:8080 you can access a Map