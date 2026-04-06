#!/usr/bin/env python3

import http.server
import os
import cgi

class SimpleHTTPRequestHandlerWithUpload(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        r, info = self.deal_post_data()
        print((r, info, "by: ", self.client_address))
        self.send_response(200)
        self.end_headers()
        response = f"<html><body><h1>Upload Result</h1><p>{info}</p><a href='/'>Back</a></body></html>"
        self.wfile.write(response.encode('utf-8'))

    def deal_post_data(self):
        content_type = self.headers['content-type']
        if not content_type:
            return (False, "Content-Type header doesn't exist")
        boundary = content_type.split("=")[1].encode('utf-8')
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content does not begin with boundary")
        line = self.rfile.readline()
        remainbytes -= len(line)
        fn = line.decode().split('filename="')[1].split('"')[0]
        path = self.translate_path(self.path)
        fn = os.path.join(path, fn)
        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)

        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")

        preline = self.rfile.readline()
        remainbytes -= len(preline)
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, f"File '{fn}' upload success!")
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpected end of data.")

    def do_GET(self):
        super().do_GET()
        self.wfile.write(b"""
        <hr>
        <form enctype="multipart/form-data" method="post">
        <input name="file" type="file"/>
        <input type="submit" value="Upload"/>
        </form>
        """)

if __name__ == '__main__':
    from http.server import HTTPServer
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandlerWithUpload)
    print("Starting HTTP server on port 8000...")
    httpd.serve_forever()
