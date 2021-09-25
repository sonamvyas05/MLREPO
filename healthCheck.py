from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from urllib.parse import urlparse
import os
import time

podtype = "arpf" #os.getenv("PODTYPE")
POD_IP = "0.0.0.0" #os.getenv('POD_IP')
healthPort = "9907" #os.getenv("HEALTH_CHECK_PORT", "9907")
started = 0


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        result = 1
        print("*****")
        #started= 30 #time.time()
        #if (self.path == '/envoyHealth'):
        if (result == 1):
          #cmd = "source ~/.bash_profile && sh /tcnVol/" + podtype + "/envoyReadiness.sh"
          #result = os.system(cmd)
           if ((time.time()-started)<=60):
             self.send_response(200)
             print("sonam")
           else :
             self.send_response(503)
             print("vyas")
           self.end_headers()

        '''if result == 0:
            self.send_response(200)
        else:
            self.send_response(503)
        self.end_headers()'''

def run(server_class=HTTPServer, handler_class=HealthCheck, port=int(healthPort)):
    #started = time.time()
    server_address = (POD_IP, port)
    httpd = server_class(server_address, handler_class)
    print(httpd)
    print("**********")
    
    print(started)
    print(time.time()-started)
    print ('Server running at ' + POD_IP + ':' + healthPort)
    httpd.serve_forever()

if ":" in POD_IP:
    run(HTTPServerV6)
else:
    #started=time.time()
    started = time.time()
    print(started)
    run()
