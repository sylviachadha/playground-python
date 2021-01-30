##-----------------------------------------
# Part 3 HTTP Server written in Python
##-----------------------------------------

import json
from http.server import BaseHTTPRequestHandler

from plots.age import get_age_count_json


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # parsed_path = parse.urlparse(self.path)
        if self.path == "/python-hiv-cases-by-age":
            response = get_age_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
