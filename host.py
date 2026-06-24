import http.server
import ssl

server_address = ('0.0.0.0', 443)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('localhost.pem')
httpd = http.server.HTTPServer(server_address,http.server.SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket,server_side=True)
httpd.serve_forever()
print('running server')