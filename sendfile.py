import http.server
import socket
from termcolor import colored
from random import randint

file2sendInput = input('Enter place and name of file to send: ')
file2send = open(file2sendInput)
response = file2send.read()
file2send.close()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode())

port = randint(0000, 9999)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
ip = s.getsockname()[0]
ipLastNumber = ip.split('.')[3]
print(f"Your code to receive file: {ipLastNumber}-{port}")
print('To receive file recipient must use same Wi-Fi network')
print(f"Press {colored('Ctrl+C','yellow')} to stop sharing")

httpd = http.server.HTTPServer(('',port), RequestHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print('\nSharing stopped.')