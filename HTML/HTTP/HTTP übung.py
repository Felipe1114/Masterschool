from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = {
    "users": [
        {"id":1,"name":"Alice"},
        {"id":2,"name":"Bob"}
    ]
}

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data["users"]).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/users":
            length = int(self.headers.get("Content-Length",0))
            body = self.rfile.read(length)
            new_user = json.loads(body)
            new_id = max(u["id"] for u in data["users"])+1 if data["users"] else 1
            new_user["id"] = new_id
            data["users"].append(new_user)
            self.send_response(201)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(new_user).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        parts = self.path.split("/")
        if len(parts) == 3 and parts[1]=="users":
            user_id = int(parts[2])
            length = int(self.headers.get("Content-Length",0))
            body = self.rfile.read(length)
            update_data = json.loads(body)
            for user in data["users"]:
                if user["id"]==user_id:
                    user.update(update_data)
                    self.send_response(200)
                    self.send_header("Content-Type","application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(user).encode())
                    return
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        parts = self.path.split("/")
        if len(parts)==3 and parts[1]=="users":
            user_id=int(parts[2])
            for i, user in enumerate(data["users"]):
                if user["id"]==user_id:
                    data["users"].pop(i)
                    self.send_response(200)
                    self.end_headers()
                    return
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8000):
    httpd = HTTPServer(('', port), SimpleHandler)
    print(f"Server läuft auf Port {port}")
    httpd.serve_forever()

if __name__=='__main__':
    run()












