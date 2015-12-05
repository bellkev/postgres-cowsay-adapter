#!/usr/bin/env python

import BaseHTTPServer
import os
import subprocess

hostname = os.environ['HOSTNAME']
port = int(os.environ['PORT'])
args = os.environ['POSTGRES_ARGS']
table = os.environ['POSTGRES_RELATION']
cmd = 'psql %s -c "select * from %s" -t | cowsay' % (args, table)

class CowHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "application/cowsay")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "application/cowsay")
        s.end_headers()
        s.wfile.write(subprocess.check_output(cmd, shell=True))

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((hostname, port), CowHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
