import socketserver
import time         # to know current time
import mimetypes    # to map filenames to MIME types
import headers      # your module 'headers.py'

debug = 0

class HTTPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # read request message
        method, path, protocol = self.rfile.readline().decode().split()

        self.parse_rfile = []
        for line in self.rfile:
            if line == b'\r\n':
                break
            self.parse_rfile.append(line)
        req_headers = {key.lower().capitalize():val for key, val in headers.parse_headers(self.parse_rfile).items()}
        content_length = req_headers.get('Content-length')
        if content_length:      # if request body exists
            body = self.rfile.read(int(content_length))
        else:
            body = None
        if debug:
            print("Method : {0}".format(method))
            print("Path : {0}".format(path))
            print("Protocol : {0}".format(protocol))
            print("Request Headers : {0}".format(req_headers))
            print("Content Length : {0}".format(content_length))
            print("Body : {0}".format(body))

        # read content from file name: '.' + path
        filename = '.' + path
        try:
            f = open(filename, 'rb')
            content = f.read()
            f.close()
        except Exception as e:
            content = None

        # Build response message
        res_headers = {}
        res_headers['Date'] = time.asctime()
        res_headers['Server'] = 'MyServer/1.0'
        res_headers['Connection'] = req_headers.get('Connection')
        if content:
            content_type, encoding = mimetypes.guess_type(filename)
            res_headers['Accept-Ranges'] = 'bytes'
            res_headers['Content-type'] = content_type
            res_headers['Content-length'] = str(len(content))
            print('HTTP/1.1 200 OK')
            self.wfile.write(b'HTTP/1.1 200 OK\r\n')
            self.wfile.write(headers.to_bytes(res_headers) + b'\r\n')
            self.wfile.write(content)
        else:
            print('HTTP/1.1 404 Not found')
            self.wfile.write(b'HTTP/1.1 404 not found\r\n')
            self.wfile.write(headers.to_bytes(res_headers) + b'\r\n')

        if debug:
            print("Response Headers : {0}".format(res_headers))

        self.wfile.flush()


http_server = socketserver.TCPServer(('', 8080), HTTPHandler)
http_server.serve_forever()