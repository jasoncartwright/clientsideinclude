import http.server as httpserver
from http.server import SimpleHTTPRequestHandler
import socketserver
from datetime import datetime

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

class TimeRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/time/' or self.path == '/time':
            # Get current time with milliseconds
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(current_time.encode('utf-8'))
        else:
            # Default behavior for other paths
            super().do_GET()

def main(port=None):
	if port is None:
		port = 8000
	handler = TimeRequestHandler
	try:
		httpd = socketserver.TCPServer(("", port), handler)
		print("serving at port", port)
		httpd.serve_forever()
	except OSError:
		print("Given PORT:{} is unavailable.Try running with diffrent PORT Number!".format(port))

if __name__ == '__main__':
	main()