from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from cgi_bin.db import add_test_data, setup_tables


def main():
    setup_tables()
    # add_test_data()
    server_addr = ('127.0.0.1', 8080)
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ["/cgi_bin"]
    server = HTTPServer(server_addr, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
