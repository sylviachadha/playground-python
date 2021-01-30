import json

from http.server import SimpleHTTPRequestHandler
from plots import dashboard_plot


class PythonHttpServer(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(PythonHttpServer, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        python_dict = {}
        if self.path == "/python-retrieve-dashboard-data":
            python_dict = dashboard_plot.all_plots_dashboard_dict()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # http response
        # self.wfile.write is response in json which goes to axios(python dictionary is converted to json here)
        self.wfile.write(json.dumps(python_dict).encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('localhost', 8080), PythonHttpServer)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
