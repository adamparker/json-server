#!/usr/bin/python3

import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http.server import HTTPStatus

class MyRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    url = self.path[1:]
    print("GET request on {}".format(self.path))
    with open(url, "rb") as fin:
      content = json.load(fin)
      print(content)
      self.send_response(HTTPStatus.OK)
      self.send_header('Content-Type', 'application/json')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      self.wfile.write(json.dumps(content).encode())
      
server = HTTPServer(('', 12345), MyRequestHandler)
print("Serving JSON files from this directory on port 12345")
server.serve_forever()
