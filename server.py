
import http.server
import socketserver
import json
import os

PORT = 9001

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/v1/modify_status':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            json_name = data.get('json_name')
            word_id = data.get('id')
            status = data.get('status')

            if not all([json_name, word_id is not None, status is not None]):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Missing parameters')
                return

            try:
                with open(json_name, 'r+') as f:
                    words = json.load(f)
                    for word in words:
                        if word.get('id') == word_id:
                            word['status'] = status
                            break
                    f.seek(0)
                    json.dump(words, f, indent=4, ensure_ascii=False)
                    f.truncate()
                
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Success')
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'JSON file not found')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            self.send_response(404)
            self.end_headers()

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
