from urllib.parse import parse_qs
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from sensorDataHandler import sensorDataHandler
import traceback

#import json

class iotServer(BaseHTTPRequestHandler):
	print("Web server running, waiting for request...")
	def do_POST(s):
		print("do_POST")
		# Respond to a POST request

		# Extract and print the cintents of the POST
		length = int(s.headers['content-length'])
		#post_data = urlparse(s.rfile.read(length).decode('utf-8'))
		post_data = s.rfile.read(length)
		parse_qs(post_data)
		#print(parse_qs(post_data))
		#data = json.loads(post_data)
		
		sensorDataHandler(post_data)
		
		print(post_data)
		#print(data)
		s.send_response(200)

if __name__ == '__main__':
	try:
		print("Starting web server...")
		HTTPServer(('####', 8080), iotServer).serve_forever()
	except:
		print("error")
		traceback.print_exc()
